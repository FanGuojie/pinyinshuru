import json


def readJson(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        jsObj = f.read()
        data = json.loads(jsObj)
    return data


EMISSION_FILE = "./data/emission.json"
TRANSITION_FILE = "./data/transition.json"
PINYIN_FILE = "./data/pinyin.json"
emission = readJson(EMISSION_FILE)
transition = readJson(TRANSITION_FILE)
pin = readJson(PINYIN_FILE)

def vertebi_2gram(c, p, sec, em=1):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n]:
            continue
        p[c+n] = emission[n][sec] * transition[c][n]*em


def vertebi_3gram(c, p, sec, third, em=1):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n] or n not in transition:
            continue
        nxt2 = transition[n]
        for n2 in nxt2:
            if n2 not in emission or third not in emission[n2]:
                continue
            p[c+n+n2] = emission[n][sec] * transition[c][n] * \
                emission[n2][third]*transition[n][n2]*em


def vertebi_4gram(c, p, sec, third, forth, em=1):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n] or n not in transition:
            continue
        nxt2 = transition[n]
        for n2 in nxt2:
            if n2 not in emission or third not in emission[n2] or n2 not in transition:
                continue
            nxt3 = transition[n2]
            for n3 in nxt3:
                if n3 not in emission or forth not in emission[n3]:
                    continue
                p[c+n+n2+n3] = emission[n][sec] * transition[c][n] * \
                    emission[n2][third]*transition[n][n2] * \
                    emission[n3][forth]*transition[n2][n3]*em


def vertebi_5gram(c, p, sec, third, forth, fifth, em=1):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n] or n not in transition:
            continue
        nxt2 = transition[n]
        for n2 in nxt2:
            if n2 not in emission or third not in emission[n2] or n2 not in transition:
                continue
            nxt3 = transition[n2]
            for n3 in nxt3:
                if n3 not in emission or forth not in emission[n3] or n3 not in transition:
                    continue
                nxt4 = transition[n3]
                for n4 in nxt4:
                    if n4 not in emission or fifth not in emission[n4]:
                        continue
                    p[c+n+n2+n3+n4] = emission[n][sec] * transition[c][n] * \
                        emission[n2][third]*transition[n][n2] * \
                        emission[n3][forth]*transition[n2][n3] * \
                        emission[n4][fifth]*transition[n3][n4] * em


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
        try:
            vertebi_4gram(c, p, sec, third, forth, emission[c][fir])
        except Exception as e:
            try:
                vertebi_3gram(c, p, sec, third, emission[c][fir])
            except Exception as e:
                vertebi_2gram(c, p, sec, emission[c][fir])
    start = max(p, key=p.get)
    return start[:2]


def gram5(start, pinyin):
    cur = start[-1]
    num = len(pinyin)
    res = start
    for i in range(2, num-3):
        p = {}
        sec = pinyin[i]
        third = pinyin[i+1]
        forth = pinyin[i+2]
        fifth = pinyin[i+3]
        vertebi_5gram(cur, p, sec, third, forth, fifth)
        if i != num-4:
            cur = max(p, key=p.get)[-4]
            res += cur
        else:
            cur = max(p, key=p.get)[-4:]
            res += cur
    return res


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
    if len(pinyin)==5:
        ngram=4
    elif len(pinyin) == 4:
        ngram = 3
    elif len(pinyin) == 3:
        ngram = 2
        
    if ngram==5:
        try:
            return gram5(start, pinyin)
        except Exception as e:
            return "这句话不能用5元模型"
    elif ngram == 4:
        try:
            return gram4(start, pinyin)
        except Exception as e:
            return "这句话不能用4元模型"
    elif ngram == 3:
        try:
            return gram3(start, pinyin)
        except Exception as e:
            return "这句话不能用3元模型"
    else:
        try:
            return gram2(start, pinyin)
        except Exception as e:
            return "这句话不能用2元模型"
