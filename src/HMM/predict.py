import json


def readJson(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        jsObj = f.read()
        data = json.loads(jsObj)
    return data


EMISSION_FILE = "./data/emission.json"
TRANSITION_FILE = "./data/transition.json"
INIT_FILE = "./data/init.json"
PINYIN_FILE = "./data/pinyin.json"
emission = readJson(EMISSION_FILE)
transition = readJson(TRANSITION_FILE)
init = readJson(INIT_FILE)
pin = readJson(PINYIN_FILE)


def vertebi_2gram(c, p, sec):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n]:
            continue
        p[c+n] = emission[n][sec] * transition[c][n]


def vertebi_3gram(c, p, sec, third):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n]:
            continue
        nxt2 = transition[n]
        for n2 in nxt2:
            if n2 not in emission or third not in emission[n2]:
                continue
            p[c+n+n2] = emission[n][sec] * transition[c][n] * \
                emission[n2][third]*transition[n][n2]


def vertebi_4gram(c, p, sec, third, forth):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n]:
            continue
        nxt2 = transition[n]
        for n2 in nxt2:
            if n2 not in emission or third not in emission[n2]:
                continue
            nxt3 = transition[n2]
            for n3 in nxt3:
                if n3 not in emission or forth not in emission[n3]:
                    continue
                p[c+n+n2+n3] = emission[n][sec] * transition[c][n] * \
                    emission[n2][third]*transition[n][n2] * \
                    emission[n3][forth]*transition[n2][n3]


def getStart(pinyin):
    fir = pinyin[0]
    sec = pinyin[1]
    third = pinyin[2]
    forth = pinyin[3]
    candi = pin[fir]
    p = {}  # for first
    for c in candi:
        if c not in transition:
            continue
        vertebi_4gram(c, p, sec, third, forth)
    return max(p, key=p.get)[:-2]


def gram4(start, pinyin):
    cur = start[-1]
    num = len(pinyin)
    res = start
    for i in range(2, num-2):
        p = {}
        sec = pinyin[i]
        third = pinyin[i+1]
        forth = pinyin[i+2]
        vertebi_4gram(cur, p, sec, third, forth)
        if i != num-3:
            cur = max(p, key=p.get)[-3]
            res += cur
        else:
            cur = max(p, key=p.get)[-3:]
            res += cur
    return res


def gram3(start, pinyin):
    cur = start[-1]
    num = len(pinyin)
    res = start
    for i in range(2, num-1):
        p = {}
        sec = pinyin[i]
        third = pinyin[i+1]
        vertebi_3gram(cur, p, sec, third)
        if i != num-2:
            cur = max(p, key=p.get)[-2]
            res += cur
        else:
            cur = max(p, key=p.get)[-2:]
            res += cur
    return res


def gram2(start, pinyin):
    cur = start[-1]
    num = len(pinyin)
    res = start
    for i in range(2, num):
        p = {}
        sec = pinyin[i]
        vertebi_2gram(cur, p, sec)
        cur = max(p, key=p.get)[-1]
        res += cur
    return res

def prep(pinyin, ngram):

    start = getStart(pinyin)
    if ngram == 4:
        return gram4(start, pinyin)
    elif ngram == 3:
        return gram3(start, pinyin)
    else:
        return gram2(start, pinyin)

