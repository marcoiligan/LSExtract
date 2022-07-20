from repository.config import Config
import requests
import xmltodict
from xml.dom import minidom
from repository.RepositoryBase import RepositoryBase
from models.order import Order
from models.payment import Payment
from models.payment_flags import Payment_Flags
from models.lineitem import LineItem
from models.li_sells import LI_Sells
from models.order_flags import Order_Flags
from models.order_totals import Order_Totals


class OrderRepository:

    def get_all_orders(self):
        conf = Config()
        orders_url = 'https://%s:%d/api/orders/?count=10&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
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
        get_response = session.get(orders_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict['orders']['@total_count']

    def get_order(self, order_id):
        conf = Config()
        order_id = order_id
        order_url = 'https://%s:%d/api/orders/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, order_id)
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
        get_response = session.get(order_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict_to_model(dict)

    def get_order_payment(self, order_id, payment_id):
        conf = Config()
        order_id = order_id
        order_url = 'https://%s:%d/api/orders/%d/payments/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, order_id,payment_id)
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
        get_response = session.get(order_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict

    def import_to_order_table(self, orders):
        repo = RepositoryBase()
        for order in orders:
            repo.insert_to_order_table(order)
        repo.con.close()

def dict_to_model(dict):
    if dict['order']['secondary_user']['user'] is not None:
        secondary_user_id = dict['order']['secondary_user']['user']['@id']
    else:
        secondary_user_id = None
    if dict['order']['order_customer']['customer'] is not None:
        customer_id = dict['order']['order_customer']['customer']['@id']
    else:
        customer_id = None
    order = Order(dict['order']['@id'], dict['order']['document_id'], dict['order']['date_created'], dict['order']['datetime_created'], dict['order']['date_modified'], dict['order']['datetime_modified'], dict['order']['storecode'], dict['order']['order_id'], customer_id, dict['order']['margin'], dict['order']['primary_user']['user']['@id'], secondary_user_id, dict['order']['printed_notes'], dict['order']['internal_notes'], dict['order']['currency']['@id'], dict['order']['terms'], dict['order']['due'], dict['order']['import_id'], dict['order']['status'], dict['order']['pricing_level'], dict['order']['c_discount_percentage'], dict['order']['web_order_number'], dict['order']['order_type'])
    get_payments(order,dict['order']['payments'])
    get_lineitems(order,dict['order']['lineitems'])
    order.set_order_flags(get_flags(dict['order']['flags']))
    order.set_order_totals(get_totals(dict['order']['totals']))
    return order

def get_payments(order,payments):
    repo = OrderRepository()
    if payments is not None:
        is_list = isinstance(payments['payment'], list)
        print(is_list)
        if not is_list:
            pay = repo.get_order_payment(int(order.id), int(payments['payment']['@id']))['payment']
            payment = Payment(pay['@id'], pay['type'], pay['payment_method'], pay['datetime_created'], pay['datetime_modified'], pay['exported'], pay['posted'], pay['number'],pay['amount'], pay['tendered'], pay['authcode'], pay['avs_result'], pay['till'])
            payment.set_payment_flags(get_payment_flags(pay['flags']))
            order.add_payments(payment)
        else:
            for x in payments['payment']:
                pay = repo.get_order_payment(int(order.id),int(x['@id']))['payment']
                payment = Payment(pay['@id'],pay['type'],pay['payment_method'],pay['datetime_created'],pay['datetime_modified'],pay['exported'],pay['posted'],pay['number'],pay['amount'],pay['tendered'],pay['authcode'],pay['avs_result'],pay['till'])
                payment.set_payment_flags(get_payment_flags(pay['flags']))
                order.add_payments(payment)

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
            lineitem = LineItem(lineitems['lineitem']['@id'], lineitems['lineitem']['quantity'], lineitems['lineitem']['sell_price'], lineitems['lineitem']['pricing_calculations'],lineitems['lineitem']['lineitem_product']['product']['@id'], None)
            lineitem.set_li_sells(get_lineitem_sells(lineitems['lineitem']['sells']))
            invoice.add_lineitems(lineitem)
        else:
            for x in lineitems['lineitem']:
                lineitem = LineItem(x['@id'],x['quantity'],x['sell_price'],x['pricing_calculations'],x['lineitem_product']['product']['@id'],None)
                lineitem.set_li_sells(get_lineitem_sells(x['sells']))
                invoice.add_lineitems(lineitem)

def get_lineitem_sells(sells):
    sells = LI_Sells(sells['sell'],sells['base'],sells['total'],sells['sell_quantity_discount'],sells['sell_tax_inclusive_quantity_discount'],sells['sell_tax_inclusive'], sells['sell_tax_inclusive_total'], sells['sell_tax_inclusive_discounted'])
    return sells

def get_flags(flags):
    flags = Order_Flags(flags['drop_shipment'])
    return flags\

def get_totals(totals):
    totals = Order_Totals(totals['cost'],totals['subtotal'],totals['profit'],totals['tax'],totals['credit'],totals['total'],totals['paid'],totals['remaining_balance'])
    return totals
