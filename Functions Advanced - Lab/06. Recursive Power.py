def recursive_power(value, power):
    if power == 0:
        return 1
    if power == 1:
        return value

    return value * recursive_power(value, power - 1)
