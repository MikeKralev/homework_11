import json


path_to_json = "candidates.json"


def load_candidates(path):
    """Read data from json file.

       Args:
           path (str) = path to file

        Returns:
            List[dict]

    """
    with open(path, encoding="utf-8") as f:
        candidates = json.load(f)
    return candidates


def get_all():
    """Returns a list of all candidates

        Returns:
            list
    """
    candidates = load_candidates(path_to_json)
    return candidates


def get_by_uid(uid):
    """Finds a candidate by his ID

        Args:
            uid (int) = user id

        Returns:
            Dict

    """
    candidates = load_candidates(path_to_json)

    result = {}
    for candidate in candidates:
        if uid == candidate["id"]:
            result = candidate
            return result


def get_by_name(name):
    """Finds candidates by name

        Args:
            name (str) = part of candidate name

        Returns:
            list

    """
    candidates = load_candidates(path_to_json)

    name_lower = name.lower()
    result = []
    for candidate in candidates:
        candidate_lower = candidate["name"].lower()
        if name_lower in candidate_lower:
            result.append({"name": candidate["name"], "id": candidate["id"]})

    return result


def get_by_skill(skill_name):
    """Finds candidates by skill

        Args:
            skill_name (str) = skill

        Returns:
            list

    """
    candidates = load_candidates(path_to_json)

    skill = skill_name.lower()
    result = []
    for candidate in candidates:
        skill_list = candidate["skills"].lower().split(', ')
        print(skill_list)
        if skill in skill_list:
            result.append({"name": candidate["name"], "id": candidate["id"]})

    return result
