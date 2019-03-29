import pickle as pkl
import math
import json


def saveJson(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def loadpkl(filename):
    with open(filename, 'rb') as f:
        pklObj = f.read()
        data = pkl.loads(pklObj)
    return data


def updateTran(tran, words, n):
    print("load pkl of %d words" %n)
    amp = pow(2*n, n)
    for w in words:
        value = words[w]
        for i in range(n-1):
            for cur, nxt in zip(w[i], w[i+1]):
                tran.setdefault(cur, {})
                tran[cur].setdefault(nxt, 0)
                tran[cur][nxt] += value*amp


def gen_transition():
    two = loadpkl('two.pkl')
    three = loadpkl('three.pkl')
    four = loadpkl('four.pkl')
    tran = {}
    updateTran(tran, two, 2)
    updateTran(tran, three, 3)
    updateTran(tran, four, 4)
    saveJson("transition.json",tran)


def main():
    gen_transition()


if __name__ == '__main__':
    main()
