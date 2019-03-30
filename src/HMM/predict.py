import json


def readJson(filename):
    print("read %s" % filename)
    with open(filename, 'r', encoding='UTF-8') as f:
        jsObj = f.read()
        data = json.loads(jsObj)
    return data


EMISSION_FILE = "./data/emission.json"
GRAM2_FILE = "./data/transition.json"
# GRAM3_FILE = "./data/transition3.json"
# GRAM4_FILE = "./data/transition4.json"
GRAM3_FILE = "./data/gram3.json"
# GRAM4_FILE = "./data/gram4.json"
PINYIN_FILE = "./data/pinyin.json"
emission = readJson(EMISSION_FILE)
gram2 = readJson(GRAM2_FILE)
gram3 = readJson(GRAM3_FILE)
# gram4 = readJson(GRAM4_FILE)
pin = readJson(PINYIN_FILE)
# gram_transition = [gram2]
gram_transition = [gram2, gram3]
# gram_transition = [gram2, gram3, gram4]
def test():
    print(gram3["我上"]['上学'])
    print(gram3['上学']['学去'])
    print(gram3['学去']['去了'])

def dfs(p, pinyin, n, res, value, ngram):
    if n == len(pinyin):
        p[res] = value
        return
    cur = res[-(ngram-1):]  # 当前gram
    nxt_yin = pinyin[n]  # 下一发音的所有可能字
    p_list = pin[nxt_yin]
    for w in p_list:  # 遍历每个可能字
        w2=cur[1:]+w
        if cur not in gram_transition[ngram-2] or w not in emission or w2 not in gram_transition[ngram-2][cur]:
            continue
        v = value * gram_transition[ngram-2][cur][w2]*emission[w][nxt_yin]
        dfs(p, pinyin, n+1, res+w, v, ngram)


def get_pre(pre_list, pre_yin, n, str):
    if n == len(pre_yin):
        pre_list.append(str)
        return
    cur_yin = pre_yin[n]
    cur_list = pin[cur_yin]
    for w in cur_list:
        get_pre(pre_list, pre_yin, n+1, str+w)


def sub_gram(pinyin, ngram):
    p = {}
    pre_yin = pinyin[0:ngram-1]  # 首gram音
    pre_list = []
    get_pre(pre_list, pre_yin, 0, "")  # 所有首音的可能
    for f in pre_list:
        em = 1
        for i in range(ngram-1):
            em *= emission[f[i]][pre_yin[i]]
        dfs(p, pinyin, ngram-1, f, em, ngram)
    return max(p, key=p.get)


def gram(pinyin, ngram):
    num = len(pinyin)
    res = ""
    up = 1+ngram  # 计算上限
    while num > 2*up:
        sub_pinyin = pinyin[:2*up]
        res += sub_gram(sub_pinyin, ngram)[:up]
        pinyin = pinyin[up:]
        num -= up
    res += sub_gram(pinyin, ngram)
    return res


def prep(pinyin, ngram):
    # test()
    if ngram == 2:
        res = gram(pinyin, 2)
    elif ngram == 3:
        res = gram(pinyin, 3)
    else:
        res = gram(pinyin, 4)

    return res
