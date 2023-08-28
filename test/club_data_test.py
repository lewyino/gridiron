from site_parser.club_data import *
import os


def test_get_club_name():
    __result = 'Unknow Team'
    f = open(f'{os.path.dirname(__file__)}/club.html', 'r')
    club_site_data = f.read()
    f.close()
    assert get_club_name(club_site_data) == __result


def test_get_club_id():
    __result = 12345
    f = open(f'{os.path.dirname(__file__)}/club.html', 'r')
    club_site_data = f.read()
    f.close()
    assert get_club_id(club_site_data) == __result
