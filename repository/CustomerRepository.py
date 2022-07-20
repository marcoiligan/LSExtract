import requests
from xml.dom import minidom
import xmltodict
from repository.config import Config
from models.customer import Customer
from models.address import Address
from models.name import Name
from models.phoneNumbers import PhoneNumber
from repository.RepositoryBase import RepositoryBase


class CustomerRepository:

    def get_all_customer(self):
        conf = Config()
        customers_url = 'https://%s:%d/api/customers/?count=6&offset=2' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to list all customers.
        get_response = session.get(customers_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        #print(dict)
        return dict['customers']['@total_count']

    def get_customer(self, customer_id):
        conf = Config()
        customer_id = customer_id
        customer_url = 'https://%s:%d/api/customers/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, customer_id)
        logout_url = 'https://%s:%d/api/sessions/current/logout/' % (conf.ONSITE_HOST, conf.ONSITE_PORT)

        # Setup a session for the http request.
        session = requests.Session()
        session.auth = (conf.ONSITE_USERNAME, conf.ONSITE_PASSWORD)
        session.headers.update({
            'user-agent': '%s/%s' % (conf.APP_ID, conf.APP_VERSION),
            'x-pappid': conf.APP_PRIVATE_ID})
        session.verify = False
        session.stream = True

        # Send the request to get a customer.
        get_response = session.get(customer_url)
        assert get_response.status_code == 200

        # Log out.
        logout_response = session.post(logout_url)
        assert logout_response.status_code == 204

        # Get the response and print it.
        response_xml = minidom.parseString(get_response.text)
        dict = xmltodict.parse(response_xml.toprettyxml())
        print(dict)
        return dictToModel(dict)

    def importToDB(self, customers):
        repo = RepositoryBase()
        for x in range(0, len(customers)):
            repo.insert_to_customer_table(customers[x])
        repo.con.close()


def dictToModel(dict):
    customer = Customer(dict['customer']['@id'], dict['customer']['created'], dict['customer']['modified'], dict['customer']['company'], dict['customer']['email'], dict['customer']['homepage'], dict['customer']['is_company'], dict['customer']['credit_hold'], dict['customer']['new_import'], dict['customer']['new_update'], dict['customer']['birthday'],  dict['customer']['credit_limit'], dict['customer']['customer_id'])
    name = Name(dict['customer']['name']['first'], dict['customer']['name']['last'])
    customer.set_Name(name)
    customer.set_BillingAddress(getAddress(dict,'billing'))
    customer.set_ShippingAddress(getAddress(dict, 'shipping'))
    getPhoneNumbers(customer, dict)

    return customer

def getAddress(dict, state):
    ad = Address()
    if state == 'billing':
        ad.address1 = dict['customer']['billing']['address']['address1']
        ad.address2 = dict['customer']['billing']['address']['address2']
        ad.city = dict['customer']['billing']['address']['city']
        ad.state = dict['customer']['billing']['address']['state']
        ad.country = dict['customer']['billing']['address']['country']
        ad.zip = dict['customer']['billing']['address']['zip']
    else:
        ad.address1 = dict['customer']['shipping']['address']['address1']
        ad.address2 = dict['customer']['shipping']['address']['address2']
        ad.city = dict['customer']['shipping']['address']['city']
        ad.state = dict['customer']['shipping']['address']['state']
        ad.country = dict['customer']['shipping']['address']['country']
        ad.zip = dict['customer']['shipping']['address']['zip']

    return ad

def getPhoneNumbers(customer,dict):
    for x in dict['customer']['phone_numbers']['phone_number']:
        phone_number = PhoneNumber(x['@id'], x['main'], x['type'], x['list_order'], x['number'])
        customer.add_PhoneNumbers(phone_number)




