from models.name import Name
from models.address import Address
from models.phoneNumbers import PhoneNumber
from models.accountStatus import AccountStatus
from models.customerCategory import CustomerCategory

class Customer:

    def __init__(self, id, created, modified, company, email, homepage, is_company, credit_hold, new_import, new_update, birthday, credit_limit, customer_id):
        self.id = id
        self.created = created
        self.modified = modified
        self.name = Name
        self.company = company
        self.email = email
        self.homepage = homepage
        self.phoneNumbers = []
        self.is_company = is_company
        self.billing = Address
        self.shipping = Address
        self.credit_hold = credit_hold
        self.new_import = new_import
        self.new_update = new_update
        self.birthday = birthday
        self.credit_limit = credit_limit
        self.customer_id = customer_id

    def set_Name(self, name):
        self.name = name

    def add_PhoneNumbers(self, phoneNumber):
        self.phoneNumbers.append(phoneNumber)

    def set_BillingAddress(self, address):
        self.billing = address

    def set_ShippingAddress(self, address):
        self.shipping = address

