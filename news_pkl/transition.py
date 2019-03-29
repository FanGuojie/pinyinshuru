import pickle as pkl
import math
import json

SENTENCES_FILE = "../sina_news/sentences.txt"


def listLoad(filename):
    res = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            res.append(l.replace('\n', ''))
    return res


def saveJson(filename, data):
    jsObj = json.dumps(data, ensure_ascii=False, indent=4)
    with open(filename, 'w') as f:
        f.write(jsObj)


def loadpkl(filename):
    with open(filename, 'rb') as f:
        pklObj = f.read()
        data = pkl.loads(pklObj)
    return data


def updateTran(tran, words, n):
    print("load pkl of %d words" % n)
    amp = pow(n, n)
    for w in words:
        value = words[w]
        for i in range(n-1):
            for cur, nxt in zip(w[i], w[i+1]):
                tran.setdefault(cur, {})
                tran[cur].setdefault(nxt, 0)
                tran[cur][nxt] += value*amp


def gen_transition():
    tran = {}
    # 通过分词获得
    two = loadpkl('two.pkl')
    three = loadpkl('three.pkl')
    four = loadpkl('four.pkl')
    updateTran(tran, two, 2)
    updateTran(tran, three, 3)
    updateTran(tran, four, 4)
    #通过文本获得
    sens=listLoad(SENTENCES_FILE)
    num=len(sens)
    j=0
    for s in sens:
        j+=1
        if j%5000==0:
            print("progress : %d / %d" %(j,num))
        for i in range(len(s)-1):
            for cur,nxt in zip(s[i],s[i+1]):
                tran.setdefault(cur,{})
                tran[cur].setdefault(nxt,0)
                tran[cur][nxt]+=1

    for t in tran:
        tran[t] = dict(
            sorted(tran[t].items(), key=lambda item: item[1], reverse=True))
    saveJson("transition.json", tran)


def main():
    gen_transition()


if __name__ == '__main__':
    main()
