from typing import List, Tuple

from model.PlayerDb import PlayerDb
from model.PlayerParse import PlayerParse


def update_player_skills(db_data: PlayerDb, parsed_data: PlayerParse) -> Tuple[PlayerDb, List[Tuple[str, int]]]:
    updated_skills = []
    p = PlayerDb(db_data.__dict__)
    p.skills = db_data.__dict__['skills'].copy()
    if p.weeks_at_club == parsed_data.weeks_at_club:
        return p, updated_skills
    for skill_name, skill_value in parsed_data.skills.items():
        if p.skills[skill_name] != skill_value:
            updated_skills.append((skill_name, skill_value - p.skills[skill_name]))
            p.skills[skill_name] = skill_value
            if skill_name in p.training_data:
                p.training_data[skill_name] = 0
        elif skill_name == parsed_data.current_training[0]:
            if skill_name in p.training_data:
                p.training_data[skill_name] = p.training_data[skill_name] + 1
            else:
                p.training_data[skill_name] = 1
    p.weeks_at_club = parsed_data.weeks_at_club
    return p, updated_skills
