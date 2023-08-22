import traceback
from typing import Tuple, List

from bs4 import BeautifulSoup


class TeamMatchArchiveParser:
    def __init__(self, data_to_parse: str):
        self.soup = BeautifulSoup(data_to_parse, 'html5lib')

    def get_seasons(self):
        try:
            form = self.soup.find('form', id='archive_form-id')
            seasons_option = form.find('select', id='selsea')
            seasons = []
            for option in seasons_option:
                seasons.append((option['value'], option.text))
            return seasons
        except:
            traceback.print_exc()
            return None

    def get_team_matches(self) -> List[Tuple[str, str, str]]:
        try:
            wrapper = self.soup.find('div', class_='rows_wrapper')
            rows = wrapper.find_all('div', recursive=False)
            matches_id = []
            for row in rows:
                try:
                    row_match_info = row.find_all('div', class_='row_cell')[1]
                    match_result_cell = row_match_info.find_all('div')[2]
                    home_team_cell = row_match_info.find_all('div')[1]
                    away_team_cell = row_match_info.find_all('div')[4]
                    match_type = row.find_all('div', class_='row_cell')[2].text.replace('\xa0', '')
                    match_result = str(match_result_cell.text).strip()
                    home_team = home_team_cell.text.strip().replace('\xa0', '')
                    away_team = away_team_cell.text.strip().replace('\xa0', '')
                    if match_result == 'vs.':
                        break
                    match_id = match_result_cell.find('a')['href'].split('/')[-1]
                    matches_id.append((match_id, match_type, home_team + ' - ' + away_team))
                except:
                    pass
            matches_id.reverse()
            return matches_id
        except:
            traceback.print_exc()
            return None
