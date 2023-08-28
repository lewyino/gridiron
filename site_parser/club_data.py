from bs4 import BeautifulSoup
import re


def get_club_name(page: str) -> str | None:
    soup = BeautifulSoup(page, 'html5lib')
    club_name_tag = soup.find('div', attrs={'id': 'club_name'})
    if not club_name_tag:
        return None
    return club_name_tag.text


def get_club_id(page: str) -> int | None:
    soup = BeautifulSoup(page, 'html5lib')
    club_id_tag = soup.find('div', attrs={'id': 'players'})
    if not club_id_tag:
        return None
    club_id = int(re.search(r'.*/(\d+)', club_id_tag.get('onclick')).groups()[0])
    return club_id
