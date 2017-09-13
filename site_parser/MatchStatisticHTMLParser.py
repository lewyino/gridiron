from html.parser import HTMLParser


class MatchStatisticHTMLParser(HTMLParser):
    result = {}
    __in_home_team = {'div': False, 'a': False}
    __in_away_team = {'div': False, 'a': False}
    __in_home_score = False
    __in_away_score = False
    __in_box_score_home = {'div': False, 'quarter': 0, 'span': False}
    __in_box_score_away = {'div': False, 'quarter': 0, 'span': False}

    def error(self, message):
        print('=== ERROR ===')
        print(message)
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'id' and attr[1] == 'home_score':
                    self.__in_home_score = True
                if attr[0] == 'id' and attr[1] == 'away_score':
                    self.__in_away_score = True
                if attr[0] == 'class' and attr[1] == 'home_team_name':
                    self.__in_home_team['div'] = True
                if attr[0] == 'class' and attr[1] == 'away_team_name':
                    self.__in_away_team['div'] = True
                if attr[0] == 'class' and attr[1] == 'boxscore_home':
                    self.__in_box_score_home['div'] = True
                if attr[0] == 'class' and attr[1] == 'boxscore_away':
                    self.__in_box_score_away['div'] = True
                if self.__in_box_score_home['div'] and attr[0] == 'class' and attr[1] == 'boxscore_quarter':
                    self.__in_box_score_home['quarter'] += 1
                if self.__in_box_score_away['div'] and attr[0] == 'class' and attr[1] == 'boxscore_quarter':
                    self.__in_box_score_away['quarter'] += 1
        if tag == 'a':
            if self.__in_home_team['div']:
                self.__in_home_team['a'] = True
            if self.__in_away_team['div']:
                self.__in_away_team['a'] = True
        if tag == 'span':
            if self.__in_box_score_home['div'] and self.__in_box_score_home['quarter']:
                self.__in_box_score_home['span'] = True
        if tag == 'span':
            if self.__in_box_score_away['div'] and self.__in_box_score_away['quarter']:
                self.__in_box_score_away['span'] = True

    def handle_endtag(self, tag):
        if tag == 'div':
            if self.__in_home_score:
                self.__in_home_score = False
            if self.__in_away_score:
                self.__in_away_score = False
            if self.__in_home_team['div']:
                self.__in_home_team['div'] = False
            if self.__in_away_team['div']:
                self.__in_away_team['div'] = False
            if self.__in_box_score_home['div'] and self.__in_box_score_home['quarter'] == 4:
                self.__in_box_score_home['div'] = False
            if self.__in_box_score_away['div'] and self.__in_box_score_away['quarter'] == 4:
                self.__in_box_score_away['div'] = False
        if tag == 'a':
            if self.__in_home_team['a']:
                self.__in_home_team['a'] = False
            if self.__in_away_team['a']:
                self.__in_away_team['a'] = False
        if tag == 'span':
            if self.__in_box_score_home['div'] and self.__in_box_score_home['span']:
                self.__in_box_score_home['span'] = False
            if self.__in_box_score_away['div'] and self.__in_box_score_away['span']:
                self.__in_box_score_away['span'] = False

    def handle_data(self, data):
        if self.__in_home_score:
            self.result['home_score'] = [int(data)]
        if self.__in_away_score:
            self.result['away_score'] = [int(data)]
        if self.__in_home_team['div'] and self.__in_home_team['a']:
            self.result['home_team'] = data
        if self.__in_away_team['div'] and self.__in_away_team['a']:
            self.result['away_team'] = data
        if self.__in_box_score_home['div'] and self.__in_box_score_home['quarter'] and self.__in_box_score_home['span']:
            self.result['home_score'].append(int(data))
        if self.__in_box_score_away['div'] and self.__in_box_score_away['quarter'] and self.__in_box_score_away['span']:
            self.result['away_score'].append(int(data))
