from site_parser.club_data import get_club_name, get_club_id
from site_scraping import get_site_session
from site_links import *


def get_data(login, password):
    session = get_site_session(login, password)
    club_name = get_club_name(session.get(SITE_CLUB).text)
    club_id = get_club_id(session.get(SITE_CLUB).text)
