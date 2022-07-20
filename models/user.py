from models.name import Name
from models.privilege_groups import Privilege_Groups


class User:

    def __init__(self, id, username, password, pin, email, account_locked, privilege_id, read_eula, hidden, enabled, phone, product, product_code, open_to_pos, gsx_apple_id, gsx_tech_id, can_open_from_otr, can_discount, internal_user, active, expired, display_welcome):
        self.id = id
        self.username = username
        self.password = password
        self.pin = pin
        self.name = Name
        self.email = email
        self.account_locked = account_locked
        self.privilege_id = privilege_id
        self.privilege_groups = Privilege_Groups
        self.read_eula = read_eula
        self.hidden = hidden
        self.enabled = enabled
        self.phone = phone
        self.product = product
        self.product_code = product_code
        self.open_to_pos = open_to_pos
        self.gsx_apple_id = gsx_apple_id
        self.gsx_tech_id = gsx_tech_id
        self.can_open_from_otr = can_open_from_otr
        self.can_discount = can_discount
        self.internal_user = internal_user
        self.active = active
        self.expired = expired
        self.display_welcome = display_welcome

    def set_name(self, name):
        self.name = name

    def set_privilege_group(self,privilege_group):
        self.privilege_groups = privilege_group
