def flights(*args):
    dict = {}
    count = 0
    current_destination = ''
    current_passengers = 0
    for arg in args:
        if arg != "Finish":
            count += 1
            if count % 2 != 0:
                current_destination = arg
                if current_destination not in dict:
                    dict[current_destination] = []

            elif count % 2 == 0:
                current_passengers = int(arg)
                dict[current_destination].append(current_passengers)
        else:
            break

    for k, v in dict.items():
        sum = 0
        for value in v:
            sum += value
        dict[k] = sum
    return dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
