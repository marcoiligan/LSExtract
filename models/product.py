from models.costs import Costs
from models.flags import Flags
from models.description import Description
from models.gl_product import GL_Product
from models.inventory import Inventory
from models.product_info import Product_Info
from models.reorder import Reorder
from models.sells import Sells
from models.classes import Classes
from models.currency import Currency
from models.pricing_level import Pricing_Level


class Product:

    def __init__(self, id, class_id, currency_id, code, sell_price, created, modified, long_web_description, family, product_id, import_id, margin, minimum_margin, notes, supplier, supplier_code, upc, multi_store_label, multi_store_master_label,serial_numbers):
        self.id = id
        self.class_id = class_id
        self.classes = Classes
        self.currency_id = currency_id
        self.currency = Currency
        self.code = code
        self.costs = Costs
        self.supplier_costs = []
        self.flags = Flags
        self.sell_price = sell_price
        self.pricing_levels = []
        self.created = created
        self.modified = modified
        self.description = Description
        self.long_web_description = long_web_description
        self.family = family
        self.gl_product = GL_Product
        self.product_id = product_id
        self.import_id = import_id
        self.inventory = Inventory
        self.margin = margin
        self.minimum_margin = minimum_margin
        self.notes = notes
        self.product_info = Product_Info
        self.reorder = Reorder
        self.sells = Sells
        self.supplier = supplier
        self.supplier_code = supplier_code
        self.upc = upc
        self.multi_store_label = multi_store_label
        self.multi_store_master_label = multi_store_master_label
        self.serial_numbers = serial_numbers

    def set_Class(self, classes):
        self.classes = classes

    def set_Currency(self, currency):
        self.currency = currency

    def set_Costs(self, cost):
        self.costs = cost

    def add_Supplier_Costs(self, cost):
        self.supplier_costs.append(cost)

    def add_Pricing_Level(self, pricing_level):
        self.pricing_levels.append(pricing_level)

    def set_Flags(self, flags):
        self.flags = flags

    def set_Description(self, description):
        self.description = description

    def set_GL_Product(self, gl_product):
        self.gl_product = gl_product

    def set_Inventory(self, inventory):
        self.inventory = inventory

    def set_Product_Info(self, product_info):
        self.product_info = product_info

    def set_Reorder(self, reorder):
        self.reorder = reorder

    def set_Sells(self, sells):
        self.sells = sells