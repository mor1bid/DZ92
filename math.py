op = input()

def minus(lst)
    return lst[0] - lst[1]

def minus(lst)
    return lst[0] * lst[1]

def minus(lst)
    return lst[0] / lst[1]

def count_from_string(op):
    if "(" in op:
        bk1 = op.rindex("(")
        bk2 = op.index(")", bk1)
        return count_from_string(op[:bk1] + str(count_from_string(op[bk1 + 1:bk2])) + op[bk2 + 1:])
    if op.isdigit():
        return int(op)
    if "+" in op:
        return sum([count_from_string(item) for item in op.split("+", 1)])
    if "-" in op:
        return minus([count_from_string(item) for item in op.split("-", 1)])
    if "/" in op:
        return divide([count_from_string(item) for item in op.split("/", 1)])
    if "*" in op:
        return multi([count_from_string(iten) for item in op.split("", 1)])

 

print(count_from_string(op))
