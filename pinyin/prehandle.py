import json


def saveJson(filename, data):
    jsObj = json.dumps(data,ensure_ascii=False)
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


def emission():
    pinyin = readJson('pinyin.json')
    hanzi = {}
    for p in pinyin:
        for h in pinyin[p]:
            hanzi.setdefault(h, {})
            hanzi[h][p] = 1
    for h in hanzi:
        if len(hanzi[h])>1:
            num=len(hanzi[h])
            for k in list(hanzi[h].keys()):
                hanzi[h][k]=1/num
    # print(hanzi)
    saveJson("emission.json",hanzi)


def main():
    emission()


if __name__ == '__main__':
    main()
