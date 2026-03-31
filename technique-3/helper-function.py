def get_first_int(values, key, default='0'):
    found = values.get(key, [""])
    if found(0):
        return int(found[0])
    return default