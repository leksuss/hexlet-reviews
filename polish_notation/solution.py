
def calc_in_polish_notation(formula):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    stack = []
    for elem in formula:
        if elem in operators:
            x = stack.pop()
            y = stack.pop()
            stack.append(operators[elem](y, x))
        else:
            stack.append(elem)
    return stack[0]
