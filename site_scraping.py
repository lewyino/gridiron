import requests
import ssl
import urllib3
from requests import Session
from site_parser.club_data import get_club_name
from site_links import *


class SslOldHttpAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')

        self.poolmanager = urllib3.poolmanager.PoolManager(
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)


__session = requests.session()
__session.mount('https://', SslOldHttpAdapter())


def get_site_session(login: str, password: str) -> Session:
    r = __session.get(SITE_CHECK)
    club_name = get_club_name(r.text)
    if not club_name:
        __session.post(SITE_LOGIN, data={'user': login, 'pass': password, 'action': 'login'})
    return __session
