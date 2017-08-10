import pycurl
import io
import re


class GridIronLogin:
    __team_id = 0
    __login = ''
    __password = ''

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def get_session(self):
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://www.grid-iron.org/home')
        s = 'user=%s&pass=%s&action=login' % (self.__login, self.__password)
        c.setopt(c.POSTFIELDS, s)
        c.setopt(c.COOKIEJAR, 'cookie.txt')
        buf = io.BytesIO()
        c.setopt(c.WRITEDATA, buf)
        c.setopt(pycurl.DNS_SERVERS, '8.8.8.8')
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.perform()

    def get_team_id(self):
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://www.grid-iron.org/club/none/Free-online-American-football-manager-game')
        c.setopt(c.COOKIEFILE, 'cookie.txt')
        buf = io.BytesIO()
        c.setopt(c.WRITEDATA, buf)
        c.setopt(pycurl.DNS_SERVERS, '8.8.8.8')
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.perform()
        data = buf.getvalue().decode('utf-8')
        re_team_id = re.search(r'https://www.grid-iron.org/club/players/team_id/(\d+)', data)
        team_id = int(re_team_id.groups()[0])
        self.__team_id = team_id
        return team_id

    def get_players_list_page(self, team_id=None):
        if not team_id:
            team_id = self.__team_id
        print('get players list page for teamid: %d' % team_id)
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://www.grid-iron.org/club/players/team_id/%d' % team_id)
        c.setopt(c.COOKIEFILE, 'cookie.txt')
        buf = io.BytesIO()
        c.setopt(c.WRITEDATA, buf)
        c.setopt(pycurl.DNS_SERVERS, '8.8.8.8')
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.perform()
        return buf.getvalue().decode('utf-8')

    @staticmethod
    def get_player_site(player_id):
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://www.grid-iron.org/club/pldetails/team_id/4775/playerid/%d' % player_id)
        c.setopt(c.COOKIEFILE, 'cookie.txt')
        buf = io.BytesIO()
        c.setopt(c.WRITEDATA, buf)
        c.setopt(pycurl.DNS_SERVERS, '8.8.8.8')
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.perform()
        return buf.getvalue().decode('utf-8')
