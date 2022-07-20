


class Product_Inventory:

    def __init__(self, id, available, reserved, coming_for_stock, coming_for_customer, warehouses, in_transit, total, product_id):
        self.id = id
        self.available = available
        self.reserved = reserved
        self.coming_for_stock = coming_for_stock
        self.coming_for_customer = coming_for_customer
        self.warehouses = warehouses
        self.in_transit = in_transit
        self.total = total
        self.product_id = product_id