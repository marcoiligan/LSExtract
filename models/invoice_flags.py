


class Invoice_Flags:

    def __init__(self, drop_shipment, exported, pay_backorders, posted, voided):
        self.drop_shipment = drop_shipment
        self.exported = exported
        self.pay_backorders = pay_backorders
        self.posted = posted
        self.voided = voided