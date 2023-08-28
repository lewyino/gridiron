from site_parser.club_data import get_club_name, get_club_id
from site_parser.players_data import get_players_list
from site_scraping import get_site_session
from site_links import *


def get_data(login, password):
    session = get_site_session(login, password)
    r = session.get(SITE_CLUB)
    club_name = get_club_name(r.content.decode(r.apparent_encoding))
    club_id = get_club_id(r.content.decode(r.apparent_encoding))
    r = session.get(SITE_PLAYERS)
    players = get_players_list(r.content.decode(r.apparent_encoding))

    # f = open('test/players.html', 'w', encoding='utf-8')
    # r = session.get(SITE_PLAYERS)
    # print(r.encoding)
    # r.content.decode(r.apparent_encoding)
    # f.write(r.content.decode(r.apparent_encoding))
    # f.close()
