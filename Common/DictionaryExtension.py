
def AppendIntoList(key, value, dict):
    if(key not in dict):
        dict[key] = []
    
    dict[key].append(value)