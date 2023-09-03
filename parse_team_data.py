from db.PlayerTinyDb import PlayerTinyDb
from model.PlayerDb import PlayerDb
from player.player_skills import update_player_skills
from site_parser.club_data import get_club_name, get_club_id
from site_parser.players_data import get_players_list, get_player_data
from site_scraping import get_site_session
from site_links import *


def get_players_data(login, password):
    session = get_site_session(login, password)
    r = session.get(SITE_CLUB)
    club_name = get_club_name(r.content.decode(r.apparent_encoding))
    club_id = get_club_id(r.content.decode(r.apparent_encoding))
    print(f'parsing data for {club_name} (id: {club_id})')
    r = session.get(SITE_PLAYERS)
    players = get_players_list(r.content.decode(r.apparent_encoding))
    print('processed... 5%')
    print(f'players in team: {len(players)}')
    percent_per_player = 95 / len(players)
    i = 0
    db = PlayerTinyDb()
    updated_player = []
    for p in players:
        i += 1
        r = session.get(SITE_PLAYER.replace('{player_id}', str(p.id)))
        new_data = get_player_data(r.content.decode(r.apparent_encoding))
        data_in_db: PlayerDb = db.get_player(p.id)
        if not data_in_db:
            data_to_save = new_data
        else:
            updated_data = update_player_skills(data_in_db, new_data)
            data_to_save = updated_data[0]
            if len(updated_data[1]) > 0:
                updated_player.append((data_to_save, updated_data[1]))
        db.save_player(data_to_save)
        print(f'processed... {round(5 + i * percent_per_player)}%')
    if len(updated_player):
        print('show updated player')
        for p in updated_player:
            print(f'{p[0].name}, update: {p[1][0][0]} ({p[1][0][1]}), current: {p[0].skills[p[1][0][0]]}')
    db.close()


    # f = open('test/players.html', 'w', encoding='utf-8')
    # r = session.get(SITE_PLAYERS)
    # print(r.encoding)
    # r.content.decode(r.apparent_encoding)
    # f.write(r.content.decode(r.apparent_encoding))
    # f.close()
