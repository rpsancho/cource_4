def is_string_in_dict(s: str, d: dict):
    return s in d['title'] or s in d['description'] or s in d['requirements']
