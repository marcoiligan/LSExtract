from repository.config import Config
import requests
import xmltodict
from xml.dom import minidom
from models.invoice import Invoice
from models.payment import Payment
from models.payment_flags import Payment_Flags
from models.lineitem import LineItem
from models.li_sells import LI_Sells
from models.invoice_flags import Invoice_Flags
from models.invoice_totals import Invoice_Totals
from repository.RepositoryBase import RepositoryBase
from models.invoice_source import Source
from models.returned_invoice import Returned_Invoice


class InvoiceRepository:

    def get_all_customer(self):
        conf = Config()
        invoices_url = 'https://%s:%d/api/invoices/?count=10&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to list all invoices.
        get_response = session.get(invoices_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict['invoices']['@total_count']

    def get_invoice(self, invoice_id):
        conf = Config()
        invoice_id = invoice_id
        invoice_url = 'https://%s:%d/api/invoices/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, invoice_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get an invoice.
        get_response = session.get(invoice_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict_to_model(dict)

    def get_invoice_payment(self, invoice_id, payment_id):
        conf = Config()
        invoice_id = invoice_id
        invoice_url = 'https://%s:%d/api/invoices/%d/payments/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, invoice_id,payment_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get an invoice.
        get_response = session.get(invoice_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict

    def import_to_invoice_table(self, invoices):
        repo = RepositoryBase()
        for invoice in invoices:
            repo.insert_to_invoice_table(invoice)
        repo.con.close()

def dict_to_model(dict):
    if dict['invoice']['secondary_user']['user'] is not None:
        secondary_user_id = dict['invoice']['secondary_user']['user']['@id']
    else:
        secondary_user_id = None
    if dict['invoice']['invoice_customer']['customer'] is not None:
        customer_id = dict['invoice']['invoice_customer']['customer']['@id']
    else:
        customer_id = None
    invoice = Invoice(dict['invoice']['@id'], dict['invoice']['document_id'], dict['invoice']['date_created'], dict['invoice']['datetime_created'], dict['invoice']['date_modified'], dict['invoice']['datetime_modified'], dict['invoice']['storecode'], dict['invoice']['invoice_id'], customer_id, dict['invoice']['margin'], dict['invoice']['primary_user']['user']['@id'], secondary_user_id, dict['invoice']['printed_notes'], dict['invoice']['internal_notes'], dict['invoice']['currency']['@id'], dict['invoice']['terms'], dict['invoice']['due'], dict['invoice']['import_id'], dict['invoice']['status'], dict['invoice']['pricing_level'], dict['invoice']['c_discount_percentage'], dict['invoice']['cc_info'], dict['invoice']['exported'], dict['invoice']['posted'], dict['invoice']['station'])
    get_payments(invoice,dict['invoice']['payments'])
    get_lineitems(invoice,dict['invoice']['lineitems'])
    invoice.set_invoice_flags(get_flags(dict['invoice']['flags']))
    invoice.set_invoice_totals(get_totals(dict['invoice']['totals']))
    get_source(invoice,dict['invoice']['source'])
    get_returned_invoice(invoice, dict['invoice']['returned_invoice'])
    return invoice

def get_payments(invoice,payments):
    repo = InvoiceRepository()
    if payments is not None:
        length = len(payments)
        is_list = isinstance(payments['payment'], list)
        print(is_list)
        if not is_list:
            pay = repo.get_invoice_payment(int(invoice.id), int(payments['payment']['@id']))['payment']
            payment = Payment(pay['@id'], pay['type'], pay['payment_method'], pay['datetime_created'], pay['datetime_modified'], pay['exported'], pay['posted'], pay['number'],pay['amount'], pay['tendered'], pay['authcode'], pay['avs_result'], pay['till'])
            payment.set_payment_flags(get_payment_flags(pay['flags']))
            invoice.add_payments(payment)
        else:
            for x in payments['payment']:
                pay = repo.get_invoice_payment(int(invoice.id),int(x['@id']))['payment']
                payment = Payment(pay['@id'],pay['type'],pay['payment_method'],pay['datetime_created'],pay['datetime_modified'],pay['exported'],pay['posted'],pay['number'],pay['amount'],pay['tendered'],pay['authcode'],pay['avs_result'],pay['till'])
                payment.set_payment_flags(get_payment_flags(pay['flags']))
                invoice.add_payments(payment)

def get_payment_flags(payment_flags):
    flags = Payment_Flags(payment_flags['exported'], payment_flags['posted'], payment_flags['voided'])
    return flags

def get_lineitems(invoice, lineitems):
    if lineitems is not None:
        length = len(lineitems)
        print(length)
        print(lineitems['lineitem'])
        is_list = isinstance(lineitems['lineitem'], list)
        if not is_list:
            lineitem = LineItem(lineitems['lineitem']['@id'], lineitems['lineitem']['quantity'], lineitems['lineitem']['sell_price'], lineitems['lineitem']['pricing_calculations'],lineitems['lineitem']['lineitem_product']['product']['@id'], lineitems['lineitem']['quantity_backordered'])
            lineitem.set_li_sells(get_lineitem_sells(lineitems['lineitem']['sells']))
            invoice.add_Lineitems(lineitem)
        else:
            for x in lineitems['lineitem']:
                lineitem = LineItem(x['@id'],x['quantity'],x['sell_price'],x['pricing_calculations'],x['lineitem_product']['product']['@id'],x['quantity_backordered'])
                lineitem.set_li_sells(get_lineitem_sells(x['sells']))
                invoice.add_Lineitems(lineitem)

def get_lineitem_sells(sells):
    sells = LI_Sells(sells['sell'],sells['base'],sells['total'],sells['sell_quantity_discount'],sells['sell_tax_inclusive_quantity_discount'],sells['sell_tax_inclusive'], sells['sell_tax_inclusive_total'], sells['sell_tax_inclusive_discounted'])
    return sells

def get_flags(flags):
    flags = Invoice_Flags(flags['drop_shipment'],flags['exported'],flags['pay_backorders'],flags['posted'],flags['voided'])
    return flags

def get_totals(totals):
    totals = Invoice_Totals(totals['cost'],totals['subtotal'],totals['profit'],totals['tax'],totals['total'],totals['owing'],totals['paid'],totals['total_backordered'],totals['remaining_balance'])
    return totals

def get_source(invoice,sources):
    if sources is not None:
        is_list = isinstance(sources,list)
        if not is_list:
            source = Source(sources['id'])
            invoice.add_source(source)
        else:
            for x in sources:
                source = Source(x['id'])
                invoice.add_source(source)
    else:
        invoice.source = None

def get_returned_invoice(invoice,return_invoice):
    if return_invoice is not None:
        is_list = isinstance(return_invoice,list)
        if not is_list:
            return_inv = Returned_Invoice(return_invoice['@id'])
            invoice.add_returned_invoice(return_inv)
        else:
            for x in return_invoice:
                return_inv = Returned_Invoice(x['@id'])
                invoice.returned_invoice(return_inv)
    else:
        invoice.returned_invoice = None