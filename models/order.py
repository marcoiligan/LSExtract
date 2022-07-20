from models.currency import Currency
from models.address import Address
from models.order_flags import Order_Flags
from models.order_totals import Order_Totals


class Order:

    def __init__(self, id, document_id, date_created, datetime_created, date_modified, datetime_modified, storecode, order_id, customer_id, margin, primary_user_id, secondary_user_id,printed_notes, internal_notes, currency_id, terms, due, import_id, status, pricing_level, c_discount_percentage, web_order_number, order_type):
        self.id = id
        self.document_id = document_id
        self.date_created = date_created
        self.datetime_created = datetime_created
        self.date_modified = date_modified
        self.datetime_modified = datetime_modified
        self.storecode = storecode
        self.order_id = order_id
        self.customer_id = customer_id
        self.margin = margin
        self.primary_user_id = primary_user_id
        self.secondary_user_id = secondary_user_id
        self.printed_notes = printed_notes
        self.internal_notes = internal_notes
        self.currency_id = currency_id
        self.currency = Currency  # no need to get
        self.terms = terms
        self.due = due
        self.import_id = import_id
        self.status = status
        self.pricing_level = pricing_level
        self.c_discount_percentage = c_discount_percentage
        self.payments = []
        self.billing = Address
        self.shipping = Address
        self.lineitems = []
        self.flags = Order_Flags
        self.totals = Order_Totals
        self.web_order_number = web_order_number
        self.order_type = order_type


    def add_payments(self, payment):
        self.payments.append(payment)

    def set_currency(self, currency):
        self.currency = currency

    def set_billing(self, address):
        self.billing = address

    def set_shipping(self, address):
        self.shipping = address

    def add_lineitems(self, lineitem):
        self.lineitems.append(lineitem)

    def set_order_flags(self, flags):
        self.flags = flags

    def set_order_totals(self, totals):
        self.totals = totals
