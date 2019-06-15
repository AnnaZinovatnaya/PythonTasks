class Device(object):
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        print('get unit_name')
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        print(f'set unit_name - {self._unit_name} -> {value}')
        self._unit_name = value

    @property
    def mac_address(self):
        print('get mac_address')
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        print(f'set mac_address - {self._mac_address} -> {value}')
        self._mac_address = value

    @property
    def ip_address(self):
        print('get ip_address')
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        print(f'set ip_address - {self._ip_address} -> {value}')
        self._ip_address = value

    @property
    def login(self):
        print('get login')
        return self._login

    @login.setter
    def login(self, value):
        print(f'set login - {self._login} -> {value}')
        self._login = value

    @property
    def password(self):
        print('get password')
        return self._password

    @password.setter
    def password(self, value):
        print(f'set password - {self._password} -> {value}')
        self._password = value


d = Device('1234', '000', '111', 'abcd', 'qwerty')
d.ip_address = '192.192.192.192'
print(d.ip_address)
