import re
from model.Player import *


class GridIronParser:

    @staticmethod
    def get_players_list(players_page):
        players = []
        re_offense = re.search(r'<div id="offense".*\W*(.+)</div>', players_page)
        players.extend(GridIronParser.__parse_team_table(re_offense.groups(0)[0]))
        re_defense = re.search(r'<div id="defense".*\W*(.+)</div>', players_page)
        players.extend(GridIronParser.__parse_team_table(re_defense.groups(0)[0]))
        re_special = re.search(r'<div id="special".*\W*(.+)</div>', players_page)
        players.extend(GridIronParser.__parse_team_table(re_special.groups(0)[0]))
        return players

    @staticmethod
    def __parse_team_table(table):
        table = str(table.strip())
        table_in_tab = re.split(r'table_row\d', table)
        players = []
        for t in table_in_tab[1:]:
            players.append(GridIronParser.__parse_team_table_row(t))
        return players

    @staticmethod
    def __parse_team_table_row(table_row):
        row = str(table_row.strip())
        row_in_tab = re.split('row_cell', row)
        read = 0
        player_data = []
        for r in row_in_tab:
            re_object = re.search(r'playerid/\d+.*">', r)
            if re.search(r'">(\d+)%', r):
                data = re.search(r'">(\d+)%', r)
                player_data.append(data.groups(0)[0])
                read += 1
            elif re.search(r'rating_(\d+).png', r):
                data = re.search(r'rating_(\d+).png', r)
                player_data.append(data.groups(0)[0])
                read += 1
            elif re.search(r'">\$ ([0-9,]+)</div>', r):
                data = re.search(r'">\$ ([0-9,]+)</div>', r)
                player_data.append(data.groups(0)[0])
                read += 1
            elif re.search(r'">(.+)</span>', r):
                data = re.search(r'<span.*">(.+)</span>', r)
                player_data.append(data.groups(0)[0])
                read += 1
            elif read > 0:
                data = re.search(r'">(\w+)</div>', r)
                player_data.append(data.groups(0)[0])
                read += 1
            elif re_object:
                read = 1
                player_id = re.search(r'playerid/(\d+).*">', r)
                player_data.append(player_id.groups(0)[0])
                player_name = re.search(r'playerid/\d+.*">(.*)</a>', r)
                player_data.append(player_name.groups(0)[0])
        player = Player(
            int(player_data[0]),
            player_data[1],
            player_data[2],
            int(player_data[3]),
            float(player_data[4]),
            int(player_data[5]),
            player_data[6],
            player_data[7]
        )
        return player

    @staticmethod
    def update_player_data(player, player_page):
        player.update_stars_data(GridIronParser.__get_stars_list(player_page))
        player_data_tab = re.split('header_wrapper', player_page)
        counter = 1
        for html in player_data_tab:
            # TODO counter += 1
            # counter += 1
            if counter >= 4:
                break
            elif re.search('player_data_wrapper', html) and counter == 1:
                player.update_skills_data(GridIronParser.__get_skills_list(html))
                counter += 1
            elif re.search('player_data_wrapper', html) and counter == 2:
                player.update_size_data(GridIronParser.__get_size_data_list(html))
                counter += 1
            elif re.search('player_data_wrapper', html) and counter == 3:
                player.update_other_data(GridIronParser.__get_other_data_list(html))
                counter += 1
        player.last_update_week = player.weeks_at_club
        return player

    @staticmethod
    def __get_stars_list(html_to_parse):
        data = re.search(r'player_basic_info_bottom[.\w\W]*rating_(\d+).png[\w\W]*rating_(\d+).png[\w\W]*rating_(\d+).png[\w\W]*rating_(\d+).png[\w\W]*detail_skills', html_to_parse)
        return data.groups()

    @staticmethod
    def __get_skills_list(html_to_parse):
        data = re.split('player_data_wrapper', html_to_parse)
        skills = []
        for row in data:
            if re.search('player_data_cell_txt', row):
                data = re.search(r'bold;[.\w\W]*>(\d+)[.\w\W]*bold;[.\w\W]*>(\d+)[.\w\W]*bold;[.\w\W]*>(\d+)[.\w\W]*bold;[.\w\W]*>(\d+)[.\w\W]*', row)
                if data:
                    skills.extend(data.groups())
                else:
                    print('wrong data __get_skills_list')
                    print(row)
        return skills

    @staticmethod
    def __get_size_data_list(html_to_parse):
        data = re.search(r'<b>(\d+)</b>[.\w\W]*<b>(\d+)</b>[.\w\W]*<b>(\d+.\d+)</b>[.\w\W]*', html_to_parse)
        return data.groups()

    @staticmethod
    def __get_other_data_list(html_to_parse):
        data = re.search(r'bold;">(\d+)[.\w\W]*bold;">(\d+)[.\w\W]*bold;">(\d+)[.\w\W]*', html_to_parse)
        return data.groups()