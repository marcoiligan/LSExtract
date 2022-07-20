import requests
from xml.dom import minidom
import xmltodict
from repository.config import Config
from models.product import Product
from models.costs import Costs
from models.supplier_cost import Supplier_Cost
from models.currency import Currency
from models.flags import Flags
from models.description import Description
from models.gl_product import GL_Product
from models.inventory import Inventory
from models.product_info import Product_Info
from models.reorder import Reorder
from models.sells import Sells
from repository.RepositoryBase import RepositoryBase
from models.pricing_level import Pricing_Level
from models.classes import Classes
from models.product_inventory import Product_Inventory


class ProductRepository:

    def get_all_product(self):
        conf = Config()
        products_url = 'https://%s:%d/api/products/?count=10&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to list all products.
        get_response = session.get(products_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        return dict['products']['@total_count']

    def get_product(self,product_id):
        conf = Config()
        product_id = product_id
        product_url = 'https://%s:%d/api/products/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, product_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get a product.
        get_response = session.get(product_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dictToModel(dict)

    def import_to_db(self, products):
        repo = RepositoryBase()
        for x in range(0, len(products)):
            repo.insert_to_product_table(products[x])
        repo.con.close()

    def get_all_classes(self):
        conf = Config()
        products_url = 'https://%s:%d/api/setup/classes/?count=10&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to list all products.
        get_response = session.get(products_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict['classes']['@total_count']

    def get_class(self, class_id):
        conf = Config()
        class_id = class_id
        product_url = 'https://%s:%d/api/setup/classes/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, class_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get a product.
        get_response = session.get(product_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict_to_class_model(dict)

    def import_to_db_classtbl(self, classes):
        repo = RepositoryBase()
        for x in range(0, len(classes)):
            repo.insert_to_classes(classes[x])
        repo.con.close()

    def get_all_currencies(self):
        conf = Config()
        products_url = 'https://%s:%d/api/setup/currencies/?count=10&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to list all products.
        get_response = session.get(products_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict['currencies']['@total_count']

    def get_currency(self, currency_id):
        conf = Config()
        currency_id = currency_id
        product_url = 'https://%s:%d/api/setup/currencies/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, currency_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get a product.
        get_response = session.get(product_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict_to_currency_model(dict)

    def import_to_db_currencytbl(self, currencies):
        repo = RepositoryBase()
        for x in range(0, len(currencies)):
            repo.insert_to_currencies(currencies[x])
        repo.con.close()

    def get_product_inventory(self, product_id):
        conf = Config()
        product_id = product_id
        product_url = 'https://%s:%d/api/product_inventory/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, product_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get a product.
        get_response = session.get(product_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dict_to_product_inventory_model(dict)

    def import_to_db_inventorytbl(self, product_inventories):
        repo = RepositoryBase()
        for inventory in product_inventories:
            repo.insert_to_inventory_table(inventory)
        repo.con.close()

def dict_to_product_inventory_model(dict):
    product_inventory = Product_Inventory(dict['product_inventory']['@id'],dict['product_inventory']['available'],dict['product_inventory']['reserved'],dict['product_inventory']['coming_for_stock'],dict['product_inventory']['coming_for_customer'],dict['product_inventory']['warehouses'],dict['product_inventory']['in_transit'],dict['product_inventory']['total'],dict['product_inventory']['product']['@id'])
    return product_inventory

def dict_to_currency_model(dict):
    currency = Currency(dict['currency']['@id'],dict['currency']['name'],dict['currency']['rate'],dict['currency']['symbol'])
    return currency

def dict_to_class_model(dict):
    classes = Classes(dict['class']['@id'],dict['class']['name'])
    return classes

def dictToModel(dict):
    product = Product(dict['product']['@id'], dict['product']['class']['@id'], dict['product']['currency']['@id'], dict['product']['code'], dict['product']['sell_price'], dict['product']['created'], dict['product']['modified'], dict['product']['long_web_description'], dict['product']['family'], dict['product']['product_id'], dict['product']['import_id'], dict['product']['margin'], dict['product']['minimum_margin'], dict['product']['notes'], dict['product']['supplier']['@id'], dict['product']['supplier_code'], dict['product']['upc'], dict['product']['multi_store_label'], dict['product']['multi_store_master_label'], dict['product']['serial_numbers'])
    product.set_Costs(getCosts(dict))
    getSupplierCosts(product, dict)
    get_pricing_levels(product,dict)
    product.set_Flags(getFlags(dict['product']['flags']))
    product.set_Description(getDescription(dict['product']['description']))
    product.set_GL_Product(getGLProducts(dict['product']['gl_product']))
    product.set_Inventory(getInventory(dict['product']['inventory']))
    product.set_Product_Info(getProductInfo(dict['product']['product_info']))
    product.set_Reorder(getReorder(dict['product']['reorder']))
    product.set_Sells(getSells(dict['product']['sells']))
    return product

def getCosts(dict):
    costs = Costs(dict['product']['costs']['cost'], dict['product']['costs']['average'], dict['product']['costs']['raw'])
    """costs.cost = dict['product']['costs']['cost']
    costs.average = dict['product']['costs']['average']
    costs.raw = dict['product']['costs']['raw']"""
    return costs

def getSupplierCosts(product,dict):
    if dict['product']['supplier_costs'] is not None:
        length = len(dict['product']['supplier_costs']['cost'])
        #print(length)
        if length == 8:
            supplier = dict['product']['supplier_costs']['cost']['supplier']
            print(supplier)
            if supplier is None:
                cost = Supplier_Cost(dict['product']['supplier_costs']['cost']['@id'],dict['product']['supplier_costs']['cost']['raw'],dict['product']['supplier_costs']['cost']['currency']['@id'],dict['product']['supplier_costs']['cost']['cost'],dict['product']['supplier_costs']['cost']['supplier'],dict['product']['supplier_costs']['cost']['supplier_product_code'],dict['product']['supplier_costs']['cost']['default'])
                cost.set_currency(getCurrency(dict['product']['supplier_costs']['cost']['currency']))
                product.add_Supplier_Costs(cost)
            else:
                cost = Supplier_Cost(dict['product']['supplier_costs']['cost']['@id'],dict['product']['supplier_costs']['cost']['raw'],dict['product']['supplier_costs']['cost']['currency']['@id'],dict['product']['supplier_costs']['cost']['cost'],dict['product']['supplier_costs']['cost']['supplier']['@id'],dict['product']['supplier_costs']['cost']['supplier_product_code'],dict['product']['supplier_costs']['cost']['default'])
                cost.set_currency(getCurrency(dict['product']['supplier_costs']['cost']['currency']))
                product.add_Supplier_Costs(cost)
        else:
            for x in dict['product']['supplier_costs']['cost']:
                supplier = x['supplier']
                if supplier is None:
                    cost = Supplier_Cost(x['@id'], x['raw'],x['currency']['@id'], x['cost'], x['supplier'], x['supplier_product_code'], x['default'])
                    cost.set_currency(getCurrency(x['currency']))
                    product.add_Supplier_Costs(cost)
                else:
                    cost = Supplier_Cost(x['@id'], x['raw'],x['currency']['@id'], x['cost'], x['supplier']['@id'], x['supplier_product_code'],x['default'])
                    cost.set_currency(getCurrency(x['currency']))
                    product.add_Supplier_Costs(cost)
    else:
        product.supplier_costs = None

def get_pricing_levels(product,dict):
    if dict['product']['pricing_levels'] is None:
        product.pricing_levels = None
    else:
        length = len(dict['product']['pricing_levels']['level'])
        print(length)
        if isinstance(dict['product']['pricing_levels']['level'], list):
            for x in dict['product']['pricing_levels']['level']:
                pricing_level = Pricing_Level(x['@index'],x['@name'],x['@sell_price'])
                product.pricing_levels.append(pricing_level)
        else:
            pricing_level = Pricing_Level(dict['product']['pricing_levels']['level']['@index'],dict['product']['pricing_levels']['level']['@name'],dict['product']['pricing_levels']['level']['@sell_price'])
            product.pricing_levels.append(pricing_level)


def getCurrency(currency):
    cur = Currency(currency['@id'],currency['name'],currency['rate'],currency['symbol'])
    return cur

def getFlags(fl):
    flags = Flags(fl['current'],fl['editable'],fl['gift_card'],fl['inventoried'],fl['new_cost'],fl['new_update'],fl['no_live_rules'],fl['no_profit'],fl['serialized'],fl['web'],fl['editable_sell'],fl['master_model'])
    return flags

def getDescription(desc):
    if len(desc) == 2:
        description = Description(desc['@short'],desc['#text'])
    else:
        description = Description('', desc)
    return description

def getGLProducts(gl):
    glProduct = GL_Product(gl['asset'],gl['cogs_expense'],gl['income'],gl['payable_expense'])
    return glProduct

def getInventory(inven):
    inventory = Inventory(inven['available'],inven['reserved'],inven['coming_for_stock'],inven['coming_for_customer'],inven['warehouses'],inven['in_transit'],inven['total'])
    return inventory

def getProductInfo(prodInfo):
    productInfo = Product_Info(prodInfo['color'],prodInfo['height'],prodInfo['length'],prodInfo['size'],prodInfo['weight'],prodInfo['width'])
    return productInfo

def getReorder(re):
    reorder = Reorder(re['amount'],re['calc'],re['point'],re['type'])
    return reorder

def getSells(se):
    sells = Sells(se['sell'],se['sell_tax_inclusive'],se['sell_web'])
    return sells



