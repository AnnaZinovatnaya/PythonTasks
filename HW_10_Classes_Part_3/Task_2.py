import pprint
import datetime


class Proxy(object):
    def __init__(self, ip, port, last_used_date, count, username, password):
        self.ip = ip
        self.port = port
        self.last_used_date = last_used_date
        self.count = count
        self.username = username
        self.password = password

    def __repr__(self):
        return 'Proxy(ip={}, port={}, last_used_date={}, count={}, username={}, password={})' \
               .format(self.ip, self.port, self.last_used_date, self.count, self.username, self.password)

    def __gt__(self, other):
        if self.last_used_date == None and other.last_used_date == None:
            return True
        if self.last_used_date == None:
            return True
        if other.last_used_date == None:
            return False
        if self.last_used_date.date() > other.last_used_date.date():
            return True
        return False


class ProxyManager(object):
    def __init__(self, path_to_file):
        self.ok = []
        self.banned = []

        with open(path_to_file, 'r') as file:
            for line in file:
                line = line.strip('\n')
                ip, port = line.split(':')
                self.ok.append(Proxy(ip, port, last_used_date=None, count=0, username=None, password=None))
        # pprint.pprint(self.ok)

    def next_proxy(self):
        item = self.ok.pop(self.ok.index(max(self.ok)))
        return item

    def back_proxy(self, proxy, status):
        proxy.count += 1
        proxy.last_used_date = datetime.date.today()

        if status.lower() == 'ok':
            self.ok.append(proxy)
        else:
            self.banned.append(proxy)

        # pprint.pprint(self.ok)
        # pprint.pprint(self.banned)


proxy_manager = ProxyManager('data.txt')
proxy_manager.back_proxy(proxy_manager.next_proxy(), 'ok')
proxy_manager.back_proxy(proxy_manager.next_proxy(), 'error')
proxy_manager.back_proxy(proxy_manager.next_proxy(), 'error')
proxy_manager.back_proxy(proxy_manager.next_proxy(), 'error')

