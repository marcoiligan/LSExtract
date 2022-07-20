from models.invoice_customer import Invoice_Customer
from models.currency import Currency
from models.address import Address
from models.invoice_flags import Invoice_Flags
from models.invoice_totals import Invoice_Totals


class Invoice:

    def __init__(self, id, document_id, date_created, datetime_created, date_modified, datetime_modified, storecode, invoice_id, customer_id, margin, primary_user_id, secondary_user_id,printed_notes, internal_notes, currency_id, terms,due, import_id, status, pricing_level, c_discount_percentage, cc_info, exported, posted, station):
        self.id = id
        self.document_id = document_id
        self.date_created = date_created
        self.datetime_created = datetime_created
        self.date_modified = date_modified
        self.datetime_modified = datetime_modified
        self.storecode = storecode
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.margin = margin
        self.primary_user_id = primary_user_id
        self.secondary_user_id = secondary_user_id
        self.printed_notes = printed_notes
        self.internal_notes = internal_notes
        self.currency_id = currency_id
        self.currency = Currency #no need to get
        self.terms = terms
        self.due = due
        self.import_id = import_id
        self.status = status
        self.pricing_level = pricing_level
        self.c_discount_percentage = c_discount_percentage
        self.payments = []
        self.billing = Address #no need to get
        self.shipping = Address #no need to get
        self.lineitems = []
        self.flags = Invoice_Flags
        self.totals = Invoice_Totals
        self.source = []
        self.returned_invoice = []
        self.cc_info = cc_info
        self.exported = exported
        self.posted = posted
        self.station = station

    def set_Currency(self, currency):
        self.currency = currency

    def set_Billing(self, billing):
        self.billing = billing

    def set_Shipping(self, shipping):
        self.shipping = shipping

    def add_Lineitems(self, lineitem):
        self.lineitems.append(lineitem)

    def set_invoice_flags(self,flags):
        self.flags = flags

    def set_invoice_totals(self, totals):
        self.totals = totals

    def add_payments(self, payment):
        self.payments.append(payment)

    def add_source(self, source):
        self.source.append(source)

    def add_returned_invoice(self, returned_invoice):
        self.returned_invoice.append(returned_invoice)
