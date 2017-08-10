from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player


def get_match_team(verbose: bool = True):
    db = PlayerSimpleDbConnect()
    used_players = []
    selected_players = []

    best_qb = db.get_best_qb_players(10)
    for p in best_qb:
        player = Player.convert_from_tuple(p)
        try:
            used_players.index(player.id)
        except:
            player.my_pos = 'QB'
            used_players.append(player.id)
            selected_players.append(player)
            break

    best_wr = db.get_best_wr_players(10)
    for p in best_wr:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'WR'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 3:
                break

    best_te = db.get_best_te_players(10)
    for p in best_te:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'TE'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            break

    best_rb = db.get_best_rb_players(10)
    for p in best_rb:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'RB'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 6:
                break

    best_mlb = db.get_best_mlb_players(15)
    for p in best_mlb:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'MLB'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 8:
                break

    best_olb = db.get_best_olb_players(15)
    for p in best_olb:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'OLB'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 10:
                break

    best_de = db.get_best_de_players(15)
    for p in best_de:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'DE'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 12:
                break

    best_cb = db.get_best_cb_players(15)
    for p in best_cb:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'CB'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 14:
                break

    best_dl = db.get_best_dl_players(15)
    for p in best_dl:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'DL'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            break

    best_ol = db.get_best_ol_players(20)
    for p in best_ol:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'OL'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 20:
                break

    best_sf = db.get_best_sf_players(25)
    for p in best_sf:
        player = Player.convert_from_tuple(p)
        try:
            player.my_pos = 'SF'
            used_players.index(player.id)
        except:
            used_players.append(player.id)
            selected_players.append(player)
            if len(used_players) == 22:
                break

    if verbose:
        for p in selected_players:
            print('%s - %s, %s' % (p.my_pos, p.name, p.bpos))

    return selected_players
