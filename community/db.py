import json
from typing import Dict

import main

default_db_file = main.app_opts['o'] + '/u21.json'


def load_data(db_file: str = None):
    if db_file is None:
        global default_db_file
        db_file = default_db_file
    try:
        fp = open(db_file, encoding="utf8")
        data = json.load(fp)
        fp.close()
        return data
    except Exception as e:
        print(e)
        return []


def save_data(data: Dict, db_file: str = None):
    if db_file is None:
        global default_db_file
        db_file = default_db_file
    try:
        fp = open(db_file, 'w', encoding= "utf8")
        json.dump(data, fp)
        fp.close()
        return True
    except Exception as e:
        print(e)
        return False
