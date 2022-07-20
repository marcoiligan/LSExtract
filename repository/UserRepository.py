from repository.config import Config
import requests
from xml.dom import minidom
import xmltodict
from models.user import User
from models.name import Name
from models.privilege_groups import Privilege_Groups
from repository.RepositoryBase import RepositoryBase

class UserRepository:

    def get_all_users(self):
        conf = Config()
        products_url = 'https://%s:%d/api/users/?showall&count=19&offset=0' % (conf.ONSITE_HOST, conf.ONSITE_PORT)
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
        users_id = []

        for user_id in dict['users']['user']:
            print(user_id['@id'])
            users_id.append(user_id['@id'])

        return users_id

    def get_user(self,user_id):
        conf = Config()
        user_id = user_id
        product_url = 'https://%s:%d/api/users/%d/' % (conf.ONSITE_HOST, conf.ONSITE_PORT, user_id)
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
        return dict_to_user_model(dict['user'])

    def import_to_user_table(self, users, privilege_groups):
        repo = RepositoryBase()
        for user in users:
            repo.insert_to_user_table(user)
        for privilege_group in privilege_groups:
            repo.insert_to_privilege_groups_table(privilege_group)
        repo.con.close()

def dict_to_user_model(user):
    user_ = User(user['@id'],user['username'],user['password'],user['pin'],user['email'],user['account_locked'],user['privilege_group']['@id'],user['read_eula'],user['hidden'],user['enabled'],user['phone'],user['product'],user['product_code'],user['open_to_pos'],user['gsx_apple_id'],user['gsx_tech_id'],user['can_open_from_otr'],user['can_discount'],user['internal_user'],user['active'],user['expired'],user['display_welcome'])
    name = Name(user['name']['first'],user['name']['last'])
    user_.set_name(name)
    privilege_group = Privilege_Groups(user['privilege_group']['@id'],user['privilege_group']['name'],user['privilege_group']['type'])
    user_.set_privilege_group(privilege_group)
    return user_
