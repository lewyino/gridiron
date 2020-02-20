import re
import traceback

from bs4 import BeautifulSoup


def get_teams_evens(data_to_parse: str, verbose: bool = False):
    try:
        soup = BeautifulSoup(data_to_parse, 'html5lib')
        comments = soup.find('div', id='comments')
        teams = {}
        team = ''
        for comment in comments:
            if not comment.has_attr('id'):
                continue
            events = comment.children
            for event in events:
                is_owner_switch_class = event.has_attr('class') and event['class'][0] == 'owner_switch'
                if is_owner_switch_class:
                    team = re.search(r'(\s+)(.+) (\d+:\d+)', event.string).groups()[1]
                    if verbose:
                        print('switch to "%s" team' % (team,))
                    if team not in teams:
                        teams[team] = {1: {}, 2: {}, 3: {}, 4: {}}
                        if verbose:
                            print('add "%s" to teams' % (team,))
                    continue
                event_down = event.find('div', class_='event_down')
                if event_down.string:
                    down = int(re.search(r'(\d+)(.*)', event_down.string).groups()[0])
                else:
                    continue
                event_type = event.find('div', class_='event_type').string
                if verbose:
                    print('down: %i, event_type: %s' % (down, event_type))
                if event_type in teams[team][down]:
                    teams[team][down][event_type] = teams[team][down][event_type] + 1
                else:
                    teams[team][down][event_type] = 1
        return teams
    except:
        traceback.print_exc()
        return None
