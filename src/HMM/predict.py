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


def dfs(p, pinyin, n, res,value):
    if n == len(pinyin):
        p[res]=value
        return
    cur=res[-1] #当前字
    nxt_yin = pinyin[n]
    p_list = pin[nxt_yin] #下一发音的所有可能字
    for w in p_list:    #遍历每个可能字
        if cur not in transition or w not in emission or w not in transition[cur]:
            continue
        v=value* transition[cur][w]*emission[w][nxt_yin]
        dfs(p,pinyin,n+1,res+w,v)


def submax(pinyin):
    p = {}
    fir_yin=pinyin[0] #首音
    fir_list=pin[fir_yin] #所有首音的可能
    for f in fir_list:
        dfs(p, pinyin, 1, f, emission[f][fir_yin])
    return max(p, key=p.get)

def prep(pinyin, ngram):
    num = len(pinyin)
    res=""
    while num>6:
        sub_pinyin=pinyin[:6]
        res+=submax(sub_pinyin)[:3]
        pinyin=pinyin[3:]
        num-=3
    res+=submax(pinyin)
    return res