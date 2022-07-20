from models.payment_flags import Payment_Flags


class Payment:

    def __init__(self, id, type, payment_method, datetime_created, datetime_modified, exported, posted, number, amount, tendered, authcode, avs_result, till):
        self.id = id
        self.type = type
        self.payment_method = payment_method
        self.datetime_created = datetime_created
        self.datetime_modified = datetime_modified
        self.exported = exported
        self.posted = posted
        self.flags = Payment_Flags
        self.number = number
        self.amount = amount
        self.tendered = tendered
        self.authcode = authcode
        self.avs_result = avs_result
        self.till = till

    def set_payment_flags(self, payment_flags):
        self.flags = payment_flags