from models.li_sells import LI_Sells

#Note Model Order Lineitem doesnt have quantity_backordered
class LineItem:

    def __init__(self, id, quantity, sell_price, pricing_calculations, product_product_id, quantity_backordered):
        self.id = id
        self.quantity = quantity
        self.sell_price = sell_price
        self.sells = LI_Sells
        self.pricing_calculations = pricing_calculations
        self.product_product_id = product_product_id
        self.quantity_backordered = quantity_backordered

    def set_li_sells(self, li_sells):
        self.sells = li_sells