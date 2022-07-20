from models.currency import Currency


class Supplier_Cost:

    def __init__(self, id, raw, currency_id, cost, supplier, supplier_product_code, default):
        self.id = id
        self.raw = raw
        self.currency_id = currency_id
        self.currency = Currency
        self.cost = cost
        self.supplier = supplier
        self.supplier_product_code = supplier_product_code
        self.default = default

    def set_currency(self, currency):
        self.currency = currency