import http.cookiejar
import re
import urllib.parse
import urllib.request


class GridIronLoginUrllib:
    __team_id = 0
    __login = ''
    __password = ''

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def get_session(self):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        data = urllib.parse.urlencode({'user': self.__login, 'pass': self.__password, 'action': 'login'})
        data = data.encode('ascii')
        url = 'https://www.grid-iron.org/home'
        req = urllib.request.Request(url=url, data=data, method='POST')
        urllib.request.urlopen(req)

    def get_team_id(self):
        url = 'https://www.grid-iron.org/'
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        re_team_id = re.search(r'https://www.grid-iron.org/club/(\d+)', data)
        team_id = int(re_team_id.groups()[0])
        print('get_team_id', team_id)
        self.__team_id = team_id
        return team_id

    def get_players_list_page(self, team_id: int = None):
        if not team_id:
            team_id = self.__team_id
        print('get players list page for teamid: %d' % team_id)
        url = 'https://www.grid-iron.org/club/players/team_id/%d' % team_id
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return data

    def get_player_site(self, player_id: int):
        url = 'https://www.grid-iron.org/club/pldetails/team_id/4775/playerid/%d' % player_id
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return data

    @staticmethod
    def get_match_statistic_site(match_id: int):
        url = 'https://www.grid-iron.org/match/match_id/%d/action/boxscore' % match_id
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return data

    @staticmethod
    def get_match_teams_site(match_id: int):
        url = 'https://www.grid-iron.org/match/match_id/%d/action/stats' % match_id
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return data
