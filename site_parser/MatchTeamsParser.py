import re

from bs4 import BeautifulSoup


class MatchTeamsParser:
    def __init__(self, data_to_parse: str):
        self.soup = BeautifulSoup(data_to_parse, 'html5lib')

    def get_home_team(self):
        divs = self.soup.find('div', attrs = {'id': 'match_left_panel_stats'})
        return self.__get_team(divs)

    def get_away_team(self):
        divs = self.soup.find('div', attrs = {'id': 'match_right_panel_stats'})
        return self.__get_team(divs)

    def __get_team(self, divs):
        team = []
        for div in divs.find_all('div', class_=['player_row2_stats', 'player_row1_stats']):
            position = div.find('div', class_='player_pos_stats').text
            player_div = div.find('div', class_='player_name_stats')
            player_id = int(player_div.a['href'].split('/')[-1])
            player_name = player_div.a.text
            img_src = div.find_all('div', class_='player_start_stats')[1].img['src']
            player_stars = int(re.search(r'rating_(\d+).png', img_src).groups()[0])
            player = {
                'player_id': player_id,
                'player_name': player_name,
                'position': position,
                'player_stars': player_stars
            }
            team.append(player)
        return team
