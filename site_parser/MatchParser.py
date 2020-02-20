import re
import traceback

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
            traceback.print_exc()
            return 0

    def get_team_evens(self, team_name: str):
        try:
            in_team_event = False
            comments = self.soup.find('div', id='comments')
            event_down_types = {1: {}, 2: {}, 3: {}, 4: {}}
            for comment in comments:
                if not comment.has_attr('id'):
                    continue
                events = comment.children
                for event in events:
                    is_owner_switch_class = event.has_attr('class') and event['class'][0] == 'owner_switch'
                    if is_owner_switch_class:
                        team = re.search(r'(\s+)(.+) (\d+:\d+)', event.string).groups()[1]
                        in_team_event = team == team_name
                        continue
                    if in_team_event:
                        event_down = event.find('div', class_='event_down')
                        if event_down.string:
                            down = int(re.search(r'(\d+)(.*)', event_down.string).groups()[0])
                        else:
                            continue
                        event_type = event.find('div', class_='event_type').string
                        if event_type in event_down_types[down]:
                            event_down_types[down][event_type] = event_down_types[down][event_type] + 1
                        else:
                            event_down_types[down][event_type] = 1
            return event_down_types
        except:
            traceback.print_exc()
            return None
