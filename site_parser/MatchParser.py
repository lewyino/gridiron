import re

from bs4 import BeautifulSoup


class MatchParser:
    def __init__(self, data_to_parse: str):
        self.soup = BeautifulSoup(data_to_parse, 'html5lib')

    def get_audience(self):
        try:
            text = self.soup.find('div', class_='venue_info').text
            audience = int(re.search(r'(\d+)', text).groups()[0])
            return audience if audience is not None else 0
        except:
            return 0
