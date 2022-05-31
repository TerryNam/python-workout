import operator

def calc(to_solve):
    opr = {"+" : operator.add,
           "-" : operator.sub,
           "*" : operator.mul,
           "/" : operator.truediv,
           "%" : operator.mod,
           "**" : operator.pow}
    op, first_s, second_s = to_solve.split()

    first = int(first_s)
    second = int(second_s)
    return opr[op](first, second)

print(calc('* 3 6'))
