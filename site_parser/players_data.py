from bs4 import BeautifulSoup, Tag
from typing import List, Dict
import re

from model.PlayerParse import PlayerParse


def get_players_list(page: str) -> List[PlayerParse]:
    soup = BeautifulSoup(page, 'html5lib')
    players = []
    for line_name in ('offense', 'defense', 'special'):
        line_data = soup.find('div', attrs={'id': line_name})
        for player_row_raw in line_data.find_all('div', recursive=False):
            player_data = player_row_raw.select('div.row_cell')
            player_raw_data = player_data.pop(1)
            player_id = re.search(r'.*/playerid/(\d+)', player_raw_data.find('a').get('href')).groups()[0]
            player_name = player_raw_data.find('a').text
            p = PlayerParse(player_id, player_name)
            players.append(p)
    return players


def __get_player_data_basic_info_top(basic_info_top: Tag) -> Dict[str, str]:
    tags = basic_info_top.select('div.player_basic_info_row')
    player_basic_info_groups = re.search(r'(.*)\s*\(ID\s*(\d+)', tags.pop(0).select('td').pop(1).text).groups()
    player_name = player_basic_info_groups[0].strip()
    player_id = player_basic_info_groups[1].strip()
    player_age = re.search(r'(\d+).*', tags.pop(1).select('td').pop(0).text).groups()[0]
    return {
        'player_name': player_name,
        'player_id': player_id,
        'player_age': player_age
    }


def __get_player_data_basic_info_bottom(basic_info_bottom: Tag) -> Dict[str, float | int]:
    player_ratings_info = basic_info_bottom.select('td')
    player_rating = re.search(r'.*rating_(\d+).*', player_ratings_info[1].find('img').get('src')).groups()[0]
    player_experience = re.search(r'.*rating_(\d+).*', player_ratings_info[3].find('img').get('src')).groups()[0]
    player_energy = player_ratings_info[5].text.replace('%', '').strip()
    player_talent = re.search(r'.*rating_(\d+).*', player_ratings_info[7].find('img').get('src')).groups()[0]
    player_team_chemistry = re.search(r'.*rating_(\d+).*', player_ratings_info[9].find('img').get('src')).groups()[0]
    player_wage_groups = re.search(r'.*(\d+),(\d+).*', player_ratings_info[11].text).groups()
    return {
        'rating': round(float(player_rating) / 2, 1),
        'experience': round(float(player_experience) / 2, 1),
        'energy': int(player_energy),
        'talent': round(float(player_talent) / 2, 1),
        'team_chemistry': round(float(player_team_chemistry) / 2, 1),
        'wage': int(player_wage_groups[0] + player_wage_groups[1])
    }


def __get_player_data_skills(player_profile: Tag) -> Dict[str, int]:
    tags = player_profile.select('div.player_data_wrapper span')
    skills = {}
    for tag in tags:
        skill_name = tag.find_parent().find_previous_sibling().text.strip().lower().replace(' ', '_')
        skill_value = tag.text.strip()
        skills[skill_name] = int(skill_value)
    return skills


def __get_player_data_body(player_profile: Tag) -> Dict[str, float]:
    tags = player_profile.select('div.player_data_wrapper b')
    body = {}
    for i in range(3):
        body_name = tags[i].find_parent().find_previous_sibling().text.strip().lower().split(' ')[0]
        body_value = tags[i].text.strip()
        body[body_name] = float(body_value)
    return body


def __get_player_data_current_training(pltrain: Tag) -> tuple[str, int, int]:
    selected = pltrain.find('option', attrs={'selected': True})
    value_text = selected.text.split('/')[1].strip().lower()
    value = selected.get('value').split('|')
    return value_text, int(value[0]), int(value[1])


def get_player_data(page: str) -> PlayerParse:
    soup = BeautifulSoup(page, 'html5lib')
    basic_info_top = soup.find('div', attrs={'class': 'player_basic_info_top'})
    player_data = __get_player_data_basic_info_top(basic_info_top)
    player = PlayerParse(player_data['player_id'], player_data['player_name'])
    player.age = int(player_data['player_age'])
    basic_info_bottom = soup.find('div', attrs={'class': 'player_basic_info_bottom'})
    for basic_data_name, basic_data_value in __get_player_data_basic_info_bottom(basic_info_bottom).items():
        setattr(player, basic_data_name, basic_data_value)
    player_profile = soup.find('div', attrs={'id': 'profile'})
    player.skills = __get_player_data_skills(player_profile)
    weeks_at_club = player.skills['weeks_at_club']
    del player.skills['weeks_at_club']
    player.weeks_at_club = weeks_at_club
    for body_name, body_value in __get_player_data_body(player_profile).items():
        setattr(player, body_name, body_value)
    pltrain = soup.find('select', attrs={'id': 'pltrain'})
    player.current_training = __get_player_data_current_training(pltrain)
    return player

