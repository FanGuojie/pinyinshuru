import json
import pypinyin
def listLoad(filename):
    res=[]
    with open(filename,'r') as f:
        for l in f.readlines():
            res.append(l.replace('\n',''))
    return res

def saveJson(filename, data):
    jsObj = json.dumps(data,ensure_ascii=False, indent=4)
    with open(filename, 'w') as f:
        f.write(jsObj)


def savePinyin():
    ws = {}
    with open('拼音汉字表.txt', 'r') as f:
        for l in f.readlines():
            l = l.replace('\n', '')
            words = l.split(' ')
            ws[words[0]] = words[1:]
    saveJson('pinyin.json', ws)
    print("save successfully")

# 读取方式


def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        jsObj = f.read()
        data = json.loads(jsObj)
    return data


def bruteHandle(hanzi):
    for h in hanzi:
        if len(hanzi[h])>1:
            num=len(hanzi[h])
            for k in list(hanzi[h].keys()):
                hanzi[h][k]=1/num


def accurateHandle(hanzi):
    # extract multi pinyin
    multip=set()
    for h in hanzi:
        if len(hanzi[h])>1:
            multip.add(h)
    sens=listLoad('sentences.txt')
    num=len(sens)
    i=0
    total=num
    for s in sens[:total]:
        i+=1
        if i%100==0:
            print("progress : %d / %d" %(i,total))
        for w in s:
            if w in multip:
                try:
                    pin=pypinyin.lazy_pinyin(s)
                    index=s.index(w)
                    p=pin[index]
                    if p[-2:]=="ve":
                        p=p.replace("ve","ue")
                    if w=="哪" and p=="nei":
                        p="na"
                    elif w=="家" and p=="ji":
                        p="jia"
                    hanzi[w][p]+=1
                    continue
                except Exception as e:
                    print("word : %s , pinyin : %s" %(w,p))
                    print(s)
                    print(pin)
                

    for w in multip:
        s=sum(hanzi[w].values())
        for k in hanzi[w]:
            hanzi[w][k]/=s




def emission():
    pinyin = readJson('pinyin.json')
    hanzi = {}
    for p in pinyin:
        for h in pinyin[p]:
            hanzi.setdefault(h, {})
            hanzi[h][p] = 1
    # bruteHandle(hanzi)
    accurateHandle(hanzi)
    saveJson("emission.json",hanzi)


def main():
    # savePinyin()
    emission()


if __name__ == '__main__':
    main()
