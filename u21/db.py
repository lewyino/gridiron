import json
from typing import Dict

db_file = 'u21.json'


def load_data():
    global db_file
    try:
        fp = open(db_file, encoding="utf8")
        data = json.load(fp)
        fp.close()
        return data
    except Exception as e:
        print(e)
        raise None


def save_data(data: Dict):
    global db_file
    try:
        fp = open(db_file, 'w', encoding="utf8")
        json.dump(data, fp)
        fp.close()
        return True
    except Exception as e:
        print(e)
        return False
