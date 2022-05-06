def even_odd(*args):
    parity = 0 if args[-1] == 'even' else 1
    result = []
    for idx in range(len(args) - 1):
        number = args[idx]
        if number % 2 == parity:
            result.append(number)
    return result
