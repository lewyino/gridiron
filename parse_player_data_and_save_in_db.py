from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from site_parser.GridIronLoginUrllib import GridIronLoginUrllib as GridIronLogin
from site_parser.GridIronParser import GridIronParser


def parse_player_data_and_save_in_db(login, password, verbose: bool = False):
    site = GridIronLogin(login, password)
    site.get_session()
    players_list_page = site.get_players_list_page(site.get_team_id())
    players = GridIronParser.get_players_list(players_list_page)

    db = PlayerSimpleDbConnect()

    if verbose:
        print('players before save: %d\n' % db.get_count_players_in_db())

    for p in players:
        GridIronParser.update_player_data(p, site.get_player_site(p.id))
        prev_player_data = db.get_player(p.id, p.weeks_at_club - 1)
        if prev_player_data is not None:
            diff = p.get_skills_difference(prev_player_data)
            if diff is not None and len(diff) > 0:
                p.last_update_week = p.weeks_at_club
            else:
                p.last_update_week = prev_player_data.last_update_week
            p.print_player_difference(prev_player_data)
        player_save_result = db.save_player(p)
        if verbose:
            print('player %s save: %r\n' % (p.name, player_save_result,))

    if verbose:
        print('players after save: %d' % db.get_count_players_in_db())
