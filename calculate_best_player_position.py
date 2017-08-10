from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from site_parser.GridIronParser import *


def calculate_best_player_position(
        players_quantity_for_position: int = 5,
        with_save: bool = False,
        verbose: bool = True
):
    db = PlayerSimpleDbConnect()
    players = db.get_all_players()
    for p in players:
        player = Player.convert_from_tuple(p)
        best_position = player.calculate_best_position(True)
        if verbose:
            print('%s bpos: %s' % (player.name, best_position))
        if with_save:
            db.save_player_calculated_bpos(player)

    if verbose:
        print('\nbest QB:')
    best_qb_players = db.get_best_qb_players(players_quantity_for_position)
    for p in best_qb_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s qb_point: %.1f, actual bpos: %s' % (player.name, player.qb_point, player.bpos))

    if verbose:
        print('\nbest RB:')
    best_rb_players = db.get_best_rb_players(players_quantity_for_position)
    for p in best_rb_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s rb_point: %.1f, actual bpos: %s' % (player.name, player.rb_point, player.bpos))

    if verbose:
        print('\nbest WR:')
    best_wr_players = db.get_best_wr_players(players_quantity_for_position)
    for p in best_wr_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s wr_point: %.1f, actual bpos: %s' % (player.name, player.wr_point, player.bpos))

    if verbose:
        print('\nbest TE:')
    best_te_players = db.get_best_te_players(players_quantity_for_position)
    for p in best_te_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s te_oint: %.1f, actual bpos: %s' % (player.name, player.te_point, player.bpos))

    if verbose:
        print('\nbest OL:')
    best_ol_players = db.get_best_ol_players(players_quantity_for_position)
    for p in best_ol_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s ol_point: %.1f, actual bpos: %s' % (player.name, player.ol_point, player.bpos))

    if verbose:
        print('\nbest DL:')
    best_dl_players = db.get_best_dl_players(players_quantity_for_position)
    for p in best_dl_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s dl_point: %.1f, actual bpos: %s' % (player.name, player.dl_point, player.bpos))

    if verbose:
        print('\nbest DE:')
    best_de_players = db.get_best_de_players(players_quantity_for_position)
    for p in best_de_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s de_point: %.1f, actual bpos: %s' % (player.name, player.de_point, player.bpos))

    if verbose:
        print('\nbest MLB:')
    best_mlb_players = db.get_best_mlb_players(players_quantity_for_position)
    for p in best_mlb_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s mlb_point: %.1f, actual bpos: %s' % (player.name, player.mlb_point, player.bpos))

    if verbose:
        print('\nbest OLB:')
    best_olb_players = db.get_best_olb_players(players_quantity_for_position)
    for p in best_olb_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s olb_point: %.1f, actual bpos: %s' % (player.name, player.olb_point, player.bpos))

    if verbose:
        print('\nbest CB:')
    best_cb_players = db.get_best_cb_players(players_quantity_for_position)
    for p in best_cb_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s cb_point: %.1f, actual bpos: %s' % (player.name, player.cb_point, player.bpos))

    if verbose:
        print('\nbest SF:')
    best_sf_players = db.get_best_sf_players(players_quantity_for_position)
    for p in best_sf_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s sf_point: %.1f, actual bpos: %s' % (player.name, player.sf_point, player.bpos))

    if verbose:
        print('\nbest K:')
    best_k_players = db.get_best_k_players(players_quantity_for_position)
    for p in best_k_players:
        player = Player.convert_from_tuple(p)
        player.calculate_best_position(True)
        if verbose:
            print('%s k_point: %.1f, actual bpos: %s' % (player.name, player.k_point, player.bpos))
