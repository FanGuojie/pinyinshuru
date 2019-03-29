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


def vertebi(c,sec,p):
    nxt = transition[c]
    for n in nxt:
        if n not in emission or sec not in emission[n]:
            continue
        p[c+n] = emission[n][sec] * transition[c][n]

def getStart(pinyin):
    fir = pinyin[0]
    sec = pinyin[1]
    candi = pin[fir]
    p = {}  # for first
    for c in candi:
        if c not in transition:
            continue
        vertebi(c,sec,p)
    return max(p, key=p.get)


def prep(pinyin):
    num = len(pinyin)
    res = getStart(pinyin)
    cur=res[-1]
    for i in range(2,num):
        p={}
        sec=pinyin[i]
        vertebi(cur,sec,p)
        cur=max(p,key=p.get)[-1]
        res+=cur
    return res
