# 1 (7kyu)

def max_multiple(divisor, bound):
    listn = []
    for i in range(1, bound+1):
        if i % divisor == 0:
            listn.append(i)
    return max(listn)


# 3 (7kyu)

def switcheroo(s):
    res = ''
    for i in s:
        if i == 'a':
            i = 'b'
        elif i == 'b':
            i = 'a'
        res += i
    return res


# 4 (7kyu)

def number(bus_stops):
    res = 0
    for i in bus_stops:
        res += i[0] - i[1]
    return res