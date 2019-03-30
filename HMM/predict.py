import json


def readJson(filename):
    with open(filename, 'r') as f:
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


def getStart(pinyin):
    fir = pinyin[0]
    sec = pinyin[1]
    third = pinyin[2]
    candi = pin[fir]
    p = {}  # for first
    for c in candi:
        if c not in transition:
            continue
        vertebi_3gram(c, p, sec, third)
    return max(p, key=p.get)[:-1]


def prep(pinyin):
    num = len(pinyin)
    res = getStart(pinyin)
    cur = res[-1]
    for i in range(2, num-1):
        p = {}
        sec = pinyin[i]
        third = pinyin[i+1]
        vertebi_3gram(cur, p, sec, third)
        cur = max(p, key=p.get)[-2]
        res += cur
        if i == num-2:
            sec = pinyin[-1]
            p = {}
            vertebi_2gram(cur, p, sec)
            cur = max(p, key=p.get)[-1]
            res += cur
    return res
