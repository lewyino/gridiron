import re

from bs4 import BeautifulSoup


class MatchStatisticParser:
    __result = {}

    def __init__(self, match_id: int, data_to_parse: str):
        self.soup = BeautifulSoup(data_to_parse, 'html5lib')
        self.__result['match_id'] = match_id

    def get_teams(self):
        home_div = self.soup.find('div', attrs = {'class': 'home_team_name'})
        home_a_href = home_div.a['href']
        home_team_id = int(re.search(r'https://www.grid-iron.org/club/team_id/(\d+)', home_a_href).groups()[0])
        home_team_name = home_div.a.text
        away_div = self.soup.find('div', attrs = {'class': 'away_team_name'})
        away_a_href = away_div.a['href']
        away_team_id = int(re.search(r'https://www.grid-iron.org/club/team_id/(\d+)', away_a_href).groups()[0])
        away_team_name = away_div.a.text
        result = {
            'home_team': {'id': home_team_id, 'name': home_team_name},
            'away_team': {'id': away_team_id, 'name': away_team_name}
        }
        self.__result = self.__update_result(result)
        return result

    def get_score(self):
        home_div = self.soup.find('div', attrs = {'class': 'boxscore_home'})
        home_divs = home_div.find_all('div', class_='boxscore_quarter')
        home_team_score = int(home_divs[4].span.text)
        home_team_quarter = list(map(lambda q: int(q.span.text), home_divs))[0:4]
        away_div = self.soup.find('div', attrs = {'class': 'boxscore_away'})
        away_divs = away_div.find_all('div', class_='boxscore_quarter')
        away_team_score = int(away_divs[4].span.text)
        away_team_quarter = list(map(lambda q: int(q.span.text), away_divs))[0:4]
        result = {
            'home_team': {'score': home_team_score, 'quarter': home_team_quarter, 'score_lost': away_team_score},
            'away_team': {'score': away_team_score, 'quarter': away_team_quarter, 'score_lost': home_team_score}
        }
        self.__result = self.__update_result(result)
        return result

    def get_scoring(self):
        scoring = []
        table = self.soup.find_all('table', class_='summary_table')[0]
        for tr in table.find_all('tr')[2:]:
            tds = tr.find_all('td')
            if len(tds) != 4:
                continue
            point_type = tds[1].text
            a_tags = tds[3].find_all('a')
            a_tag = a_tags[0]
            if point_type == 'TD' and len(a_tags) == 2:
                a_tag = a_tags[1]
            player_id = int(a_tag['href'].split('/')[-1])
            player_name = a_tag.text
            scoring.append({
                'point_type': point_type,
                'player_id': player_id,
                'player_name': player_name
            })
        self.__result['scoring'] = scoring
        return scoring

    def get_teams_stat(self):
        result = {
            'home_team': {},
            'away_team': {}
        }
        table = self.soup.find_all('table', class_='summary_table')[1]
        trs = list(filter(lambda tr: len(tr.find_all('td')) > 0, table.find_all('tr')[3:]))
        tds_yards = trs[0].find_all('td')
        result['home_team']['total_yards'] = int(tds_yards[1].b.text)
        result['away_team']['total_yards'] = int(tds_yards[2].b.text)
        tds_passing = trs[2].find_all('td')
        result['home_team']['passing_yards'] = int(tds_passing[1].text)
        result['away_team']['passing_yards'] = int(tds_passing[2].text)
        tds_rushing = trs[8].find_all('td')
        result['home_team']['rushing_yards'] = int(tds_rushing[1].text)
        result['away_team']['rushing_yards'] = int(tds_rushing[2].text)
        tds_tackles = trs[18].find_all('td')
        result['home_team']['tackles'] = int(tds_tackles[1].text)
        result['away_team']['tackles'] = int(tds_tackles[2].text)
        tds_sacks = trs[19].find_all('td')
        result['home_team']['sacks'] = int(tds_sacks[1].text)
        result['away_team']['sacks'] = int(tds_sacks[2].text)
        tds_interceptions = trs[20].find_all('td')
        result['home_team']['interceptions'] = int(tds_interceptions[1].text)
        result['away_team']['interceptions'] = int(tds_interceptions[2].text)
        tds_fumbles = trs[21].find_all('td')
        result['home_team']['fumbles'] = int(tds_fumbles[1].text)
        result['away_team']['fumbles'] = int(tds_fumbles[2].text)
        tds_fg = trs[23].find_all('td')
        result['home_team']['fg'] = int(tds_fg[1].text)
        result['away_team']['fg'] = int(tds_fg[2].text)
        self.__result = self.__update_result(result)
        return result

    def get_teams_passing(self):
        home_table = self.soup.find_all('table', class_='summary_table')[2]
        away_table = self.soup.find_all('table', class_='summary_table')[3]
        home_tr = home_table.find_all('tr')
        away_tr = away_table.find_all('tr')
        result = {
            'home_team': {'passing': self.__get_team_passing(home_tr[2] if len(home_tr) > 2 else None)},
            'away_team': {'passing': self.__get_team_passing(away_tr[2] if len(away_tr) > 2 else None)}
        }
        self.__result = self.__update_result(result)
        result['home_team'] = result['home_team']['passing']
        result['away_team'] = result['away_team']['passing']
        return result

    def __get_team_passing(self, tr):
        if tr is None:
            return None
        tds = tr.find_all('td')
        a_tag = tds[0].a
        player_id = int(a_tag['href'].split('/')[-1])
        player_name = a_tag.text
        return {
            'player_id': player_id,
            'player_name': player_name,
            'comp': int(tds[1].text),
            'att': int(tds[2].text),
            'pct': float(tds[3].text.split(' ')[0]),
            'yds': int(tds[4].text),
            'yds_a': float(tds[5].text),
            'lng': int(tds[6].text),
        }

    def get_teams_rushing(self):
        home_table = self.soup.find_all('table', class_='summary_table')[4]
        away_table = self.soup.find_all('table', class_='summary_table')[5]
        result = {
            'home_team': {'rushing': self.__get_team_rushing(home_table.find_all('tr')[2:])},
            'away_team': {'rushing': self.__get_team_rushing(away_table.find_all('tr')[2:])}
        }
        self.__result = self.__update_result(result)
        result['home_team'] = result['home_team']['rushing']
        result['away_team'] = result['away_team']['rushing']
        return result

    def __get_team_rushing(self, trs):
        result = []
        for tr in trs:
            tds = tr.find_all('td')
            a_tag = tds[0].a
            player_id = int(a_tag['href'].split('/')[-1])
            player_name = a_tag.text
            result.append({
                'player_id': player_id,
                'player_name': player_name,
                'att': int(tds[1].text),
                'yds': int(tds[2].text),
                'yds_a': float(tds[3].text),
                'lng': int(tds[4].text),
            })
        return result

    def get_teams_receiving(self):
        home_table = self.soup.find_all('table', class_='summary_table')[6]
        away_table = self.soup.find_all('table', class_='summary_table')[7]
        result = {
            'home_team': {'receiving': self.__get_team_receiving(home_table.find_all('tr')[2:])},
            'away_team': {'receiving': self.__get_team_receiving(away_table.find_all('tr')[2:])}
        }
        self.__result = self.__update_result(result)
        result['home_team'] = result['home_team']['receiving']
        result['away_team'] = result['away_team']['receiving']
        return result

    def __get_team_receiving(self, trs):
        result = []
        for tr in trs:
            tds = tr.find_all('td')
            a_tag = tds[0].a
            player_id = int(a_tag['href'].split('/')[-1])
            player_name = a_tag.text
            result.append({
                'player_id': player_id,
                'player_name': player_name,
                'rec': int(tds[1].text),
                'yds': int(tds[2].text),
                'avg': float(tds[3].text),
                'lng': int(tds[4].text),
            })
        return result

    def get_teams_kicking(self):
        home_table = self.soup.find_all('table', class_='summary_table')[10]
        away_table = self.soup.find_all('table', class_='summary_table')[11]
        home_tr = home_table.find_all('tr')
        away_tr = away_table.find_all('tr')
        result = {
            'home_team': {'kicking': self.__get_team_kicking(home_tr[2] if len(home_tr) > 2 else None)},
            'away_team': {'kicking': self.__get_team_kicking(away_tr[2] if len(away_tr) > 2 else None)}
        }
        self.__result = self.__update_result(result)
        result['home_team'] = result['home_team']['kicking']
        result['away_team'] = result['away_team']['kicking']
        return result

    def __get_team_kicking(self, tr):
        if tr is None:
            return None
        tds = tr.find_all('td')
        a_tag = tds[0].a
        player_id = int(a_tag['href'].split('/')[-1])
        player_name = a_tag.text
        return {
            'player_id': player_id,
            'player_name': player_name,
            'fgm': int(tds[1].text),
            'fga': int(tds[2].text),
            'pct': float(tds[3].text.split(' ')[0]),
            'lng': int(tds[4].text),
        }

    def get_teams_defense(self):
        home_table = self.soup.find_all('table', class_='summary_table')[8]
        away_table = self.soup.find_all('table', class_='summary_table')[9]
        result = {
            'home_team': {'defense': self.__get_team_defense(home_table.find_all('tr')[2:])},
            'away_team': {'defense': self.__get_team_defense(away_table.find_all('tr')[2:])}
        }
        self.__result = self.__update_result(result)
        result['home_team'] = result['home_team']['defense']
        result['away_team'] = result['away_team']['defense']
        return result

    def __get_team_defense(self, trs):
        result = []
        for tr in trs:
            tds = tr.find_all('td')
            a_tag = tds[0].a
            player_id = int(a_tag['href'].split('/')[-1])
            player_name = a_tag.text
            result.append({
                'player_id': player_id,
                'player_name': player_name,
                'tackles': int(tds[1].text),
                'sacks': int(tds[2].text),
                'interceptions': int(tds[3].text),
                'fumbles': int(tds[4].text),
            })
        return result

    def __update_result(self, result):
        result_home_team = self.__result['home_team'] if 'home_team' in self.__result else {}
        result_away_team = self.__result['away_team'] if 'away_team' in self.__result else {}
        result_home_team.update(result['home_team'])
        result_away_team.update(result['away_team'])
        return {
            'match_id': self.__result['match_id'],
            'scoring': self.__result['scoring'] if 'home_team' in self.__result else [],
            'home_team': result_home_team,
            'away_team': result_away_team,
        }

    def get_result(self):
        return self.__result
