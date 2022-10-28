msg = input()

def minus(lst):
    return lst[0] - lst[1]

def multi(lst):
    return lst[0] * lst[1]

def divide(lst):
    return lst[0] / lst[1]

def count_from_string(msg):
    if "(" in msg:
        bk1 = msg.rindex("(")
        bk2 = msg.index(")", bk1)
        return count_from_string(msg[:bk1] + str(count_from_string(msg[bk1 + 1:bk2])) + msg[bk2 + 1:])
    if msg.isdigit():
        return int(msg)
    if "+" in msg:
        return sum([count_from_string(item) for item in msg.split("+", 1)])
    if "-" in msg:
        return minus([count_from_string(item) for item in msg.split("-", 1)])
    if "/" in msg:
        return divide([count_from_string(item) for item in msg.split("/", 1)])
    if "*" in msg:
        return multi([count_from_string(item) for item in msg.split("*", 1)])

print(f'The answer is: {count_from_string(msg)}')