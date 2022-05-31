def start_spring(**kwargs):
    dict = {}
    for k, v in kwargs.items():
        if v not in dict:
            dict[v] = []
        dict[v].append(k)
    sorted_dict = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for i in sorted_dict:
        type_obj = i[0]
        sorted_tuple = sorted(i[1])
        result += f'{type_obj}:\n'
        for smt in sorted_tuple:
            result += f'-{smt}\n'
    return result.strip()
