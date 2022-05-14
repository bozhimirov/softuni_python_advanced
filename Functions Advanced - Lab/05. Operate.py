def operate(operation, *args):
    def add(*args):
        result = 0
        for v in args:
            result += v
        return result

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for v in args:
            result *= v
        return result

    def divide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)
