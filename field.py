import seabattle
import methods


def inp():
    i = 0
    n = []
    while i<5:
        l = input()
        if methods.check(l) == True and methods.d[l] not in n:
            n.append(methods.d[l])
            i += 1
        else:
            print('An error appeared')
    return n

print(inp())


def fill(victim, filler):
    for k in filler:
        victim[k] = 1
    return
