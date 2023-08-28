from bs4 import BeautifulSoup
from typing import List
import re

from model.TeamPlayer import TeamPlayer


def get_players_list(page: str) -> List[TeamPlayer]:
    soup = BeautifulSoup(page, 'html5lib')
    players = []
    for line_name in ('offense', 'defense', 'special'):
        line_data = soup.find('div', attrs={'id': line_name})
        for player_row_raw in line_data.find_all('div', recursive=False):
            player_data = player_row_raw.select('div.row_cell')
            # player_country = player_data.pop(0).find('img').get('alt')
            player_raw_data = player_data.pop(1)
            player_id = re.search(r'.*/playerid/(\d+)', player_raw_data.find('a').get('href')).groups()[0]
            player_name = player_raw_data.find('a').text
            # player_bpos = player_data.pop(0).text
            # player_age = player_data.pop(0).text
            # player_rating = re.search(r'.*rating_(\d+).*', player_data.pop(0).find('img').get('src')).groups()[0]
            # player_energy = player_data.pop(0).text.replace('%', '')
            # player_wage = player_data.pop(0).text.replace('$', '').strip()
            # player_health = player_data.pop(0).text
            p = TeamPlayer(player_id, player_name)
            players.append(p)
    return players
