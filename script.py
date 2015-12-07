__author__ = 'flangelier'

day = ''

import re

def launch(day):
    if day in ('', '1'):
        print("Day 1")
        print("\tChallenge 1:", d1c1())
        print("\tChallenge 2:", d1c2())

    if day in ('', '2'):
        print("Day 2")
        print("\tChallenge 1:", d2c1())
        print("\tChallenge 2:", d2c2())

    if day in ('', '3'):
        print("Day 3")
        print("\tChallenge 1:", d3c1())
        print("\tChallenge 2:", d3c2())

    if day in ('', '4'):
        print("Day 4")
        print("\tChallenge 1:", d4c1())
        print("\tChallenge 2:", d4c2())

    if day in ('', '5'):
        print("Day 5")
        print("\tChallenge 1:", d5c1())
        print("\tChallenge 2:", d5c2())

    if day in ('', '6'):
        print("Day 6")
        print("\tChallenge 1:", d6c1())
        print("\tChallenge 2:", d6c2())

    if day in ('', '7'):
        print("Day 7")
        print("\tChallenge 1:", d7c1())
        print("\tChallenge 2:", d7c2())

    if day in ('', '8'):
        print("Day 8")
        print("\tChallenge 1:", d8c1())
        print("\tChallenge 2:", d8c2())

    if day in ('', '9'):
        print("Day 9")
        print("\tChallenge 1:", d9c1())
        print("\tChallenge 2:", d9c2())

    if day in ('', '10'):
        print("Day 10")
        print("\tChallenge 1:", d10c1())
        print("\tChallenge 2:", d10c2())

    if day in ('', '11'):
        print("Day 11")
        print("\tChallenge 1:", d11c1())
        print("\tChallenge 2:", d11c2())

    if day in ('', '12'):
        print("Day 12")
        print("\tChallenge 1:", d12c1())
        print("\tChallenge 2:", d12c2())

    if day in ('', '13'):
        print("Day 13")
        print("\tChallenge 1:", d13c1())
        print("\tChallenge 2:", d13c2())

    if day in ('', '14'):
        print("Day 14")
        print("\tChallenge 1:", d14c1())
        print("\tChallenge 2:", d14c2())

    if day in ('', '15'):
        print("Day 15")
        print("\tChallenge 1:", d15c1())
        print("\tChallenge 2:", d15c2())

    if day in ('', '16'):
        print("Day 16")
        print("\tChallenge 1:", d16c1())
        print("\tChallenge 2:", d16c2())

    if day in ('', '17'):
        print("Day 17")
        print("\tChallenge 1:", d17c1())
        print("\tChallenge 2:", d17c2())

    if day in ('', '18'):
        print("Day 18")
        print("\tChallenge 1:", d18c1())
        print("\tChallenge 2:", d18c2())

    if day in ('', '19'):
        print("Day 19")
        print("\tChallenge 1:", d19c1())
        print("\tChallenge 2:", d19c2())

    if day in ('', '20'):
        print("Day 20")
        print("\tChallenge 1:", d20c1())
        print("\tChallenge 2:", d20c2())

    if day in ('', '21'):
        print("Day 21")
        print("\tChallenge 1:", d21c1())
        print("\tChallenge 2:", d21c2())

    if day in ('', '22'):
        print("Day 22")
        print("\tChallenge 1:", d22c1())
        print("\tChallenge 2:", d22c2())

    if day in ('', '23'):
        print("Day 23")
        print("\tChallenge 1:", d23c1())
        print("\tChallenge 2:", d23c2())

    if day in ('', '24'):
        print("Day 24")
        print("\tChallenge 1:", d24c1())
        print("\tChallenge 2:", d24c2())

    if day in ('', '25'):
        print("Day 25")
        print("\tChallenge 1:", d25c1())
        print("\tChallenge 2:", d25c2())

def get_data_from_file(path):
    f = open("inputs/" + path, 'r')
    s = f.read()
    f.close()
    return s

def d1c1():
    directions = get_data_from_file('day1')
    y = 0
    for c in directions:
        if c == '(':
            y += 1
        elif c == ')':
            y -= 1
        else:
            print(c, "Not supposed to happen...")
    return y

def d1c2():
    directions = get_data_from_file('day1')
    y = 0
    for i, c in enumerate(directions):
        if c == '(':
            y += 1
        elif c == ')':
            y -= 1
        else:
            print(c, "Not supposed to happen...")
        if y == -1:
            return i + 1
    return 0

def d2c1():
    sizes = get_data_from_file("day2")
    total = 0
    for size in sizes.split('\n'):
        dim = size.split('x')
        l = int(dim[0])
        w = int(dim[1])
        h = int(dim[2])
        lw = l*w
        wh = w*h
        hl = h*l
        total += 2*(l*w + w*h + h*l) + min(lw, wh, hl)
    return total

def d2c2():
    sizes = get_data_from_file("day2")
    total = 0
    for size in sizes.split('\n'):
        dim = size.split('x')
        l = int(dim[0])
        w = int(dim[1])
        h = int(dim[2])
        total += 2*(l+w+h - max(l, w, h)) + l*w*h
    return total

def d3_get_dict(directions):
    from collections import defaultdict

    x = 0
    y = 0
    dic = defaultdict(lambda: 0)
    dic[x, y] = 1
    for c in directions:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1
        else:
            print(c, "Not supposed to happen...")
        dic[x, y] += 1
    return dic

def d3c1():
    directions = get_data_from_file('day3')
    return len(d3_get_dict(directions))

def d3c2():
    directions = get_data_from_file('day3')
    santa = ''
    robot = ''
    for i in range(0, len(directions), 2):
        santa += (directions[i])
        robot += (directions[i+1])
    dic = d3_get_dict(santa)
    dic.update(d3_get_dict(robot))
    return len(dic)

def d4c1():
    secret = get_data_from_file("day4")
    index = 0

    import hashlib
    while True:
        to_md5 = secret+str(index)
        md5string = hashlib.md5(to_md5.encode()).hexdigest()
        if md5string.startswith('00000'):
            return index
        index += 1

def d4c2():
    secret = get_data_from_file("day4")
    index = 0

    import hashlib
    while True:
        to_md5 = secret+str(index)
        md5string = hashlib.md5(to_md5.encode()).hexdigest()
        if md5string.startswith('000000'):
            return index
        index += 1

def d5c1():
    list_name = get_data_from_file("day5")
    count = 0
    for name in list_name.split('\n'):
        if "ab" in name or "cd" in name or "pq" in name or "xy" in name \
                or len(re.findall('[aeiuo]', name)) < 3:
            continue

        for index in range(0, len(name) - 1):
            if name[index] == name[index + 1]:
                count += 1
                break
    return count

def d5c2():
    list_name = get_data_from_file("day5")
    count = 0
    for name in list_name.split('\n'):
        pass1 = False
        pass2 = False
        for index in range(0, len(name) - 1):
            if not pass1 and index + 2 < len(name):
                for index2 in range(index + 2, len(name) - 1):
                    if name[index] == name[index2] and \
                                    name[index + 1] == name[index2 + 1]:
                        pass1 = True
                        break

            if (not pass2) and index + 2 < len(name) and name[index] == name[index + 2]:
                pass2 = True

            if pass1 and pass2:
                count += 1
                break
    return count

def d6c1():
    commands = get_data_from_file('day6')
    ligths = 0
    prog = re.compile("^([^\d]*)([0-9]{1,3}),([0-9]{1,3})\sthrough\s([0-9]{1,3}),([0-9]{1,3})$")
    matrix = [[0]*1000 for _ in range(1000)]

    for full_cmd in commands.split('\n'):
        _, cmd, sx1, sy1, sx2, sy2, _ = prog.split(full_cmd)
        x1 = int(sx1)
        y1 = int(sy1)
        x2 = int(sx2)
        y2 = int(sy2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if "toggle" in cmd:
                    matrix[x][y] = (matrix[x][y] + 1) % 2
                elif "turn on" in cmd:
                    matrix[x][y] = 1
                elif "turn off" in cmd:
                    matrix[x][y] = 0
    for x in range(1000):
            for y in range(1000):
                if matrix[x][y] == 1:
                    ligths += 1
    return ligths

def d6c2():
    commands = get_data_from_file('day6')
    brithness = 0
    prog = re.compile("^([^\d]*)([0-9]{1,3}),([0-9]{1,3})\sthrough\s([0-9]{1,3}),([0-9]{1,3})$")
    matrix = [[0]*1000 for _ in range(1000)]

    for full_cmd in commands.split('\n'):
        _, cmd, sx1, sy1, sx2, sy2, _ = prog.split(full_cmd)
        x1 = int(sx1)
        y1 = int(sy1)
        x2 = int(sx2)
        y2 = int(sy2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if "toggle" in cmd:
                    matrix[x][y] += 2
                elif "turn on" in cmd:
                    matrix[x][y] += 1
                elif "turn off" in cmd and matrix[x][y] > 0:
                    matrix[x][y] -= 1
    for x in range(1000):
            for y in range(1000):
                brithness += matrix[x][y]
    return brithness

def d7c1():
    return ''

def d7c2():
    return ''

def d8c1():
    return ''

def d8c2():
    return ''

def d9c1():
    return ''

def d9c2():
    return ''

def d10c1():
    return ''

def d10c2():
    return ''

def d11c1():
    return ''

def d11c2():
    return ''

def d12c1():
    return ''

def d12c2():
    return ''

def d13c1():
    return ''

def d13c2():
    return ''

def d14c1():
    return ''

def d14c2():
    return ''

def d15c1():
    return ''

def d15c2():
    return ''

def d16c1():
    return ''

def d16c2():
    return ''

def d17c1():
    return ''

def d17c2():
    return ''

def d18c1():
    return ''

def d18c2():
    return ''

def d19c1():
    return ''

def d19c2():
    return ''

def d20c1():
    return ''

def d20c2():
    return ''

def d21c1():
    return ''

def d21c2():
    return ''

def d22c1():
    return ''

def d22c2():
    return ''

def d23c1():
    return ''

def d23c2():
    return ''

def d24c1():
    return ''

def d24c2():
    return ''

def d25c1():
    return ''

def d25c2():
    return ''


launch(day)