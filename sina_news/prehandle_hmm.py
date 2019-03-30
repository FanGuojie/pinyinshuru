import json
import re
import pypinyin
import os
def saveJson(filename,data):
    jsObj = json.dumps(data,ensure_ascii=False, indent=4)
    with open(filename, 'w') as f:
        f.write(jsObj)

def readtxt(filename):
    with open(filename, 'r',encoding='gbk') as f:
        data = f.read()
    return data

def listLoad(filename):
    res=[]
    with open(filename,'r') as f:
        for l in f.readlines():
            res.append(l.replace('\n',''))
    return res

def listSave(filename, data):
    with open(filename, 'w') as f:
        for d in data:
            f.write(d+'\n')


def Decode(v):
    if v is None:
        return None
    elif isinstance(v, bytes):
        return v.decode('unicode_escape')
    elif isinstance(v, str):
        return v.encode('utf-8').decode('unicode_escape')
    else:
        raise ValueError('Unknown type %r' % type(v))


def gen_sentences():
    ARTICLE_DIR     = '../sina_news_gbk'
    SENTENCE_FILE   = './sentence.txt'
    print("generate sentences")
    sentences = []
    for root, directories, filenames in os.walk(ARTICLE_DIR):
        for filename in filenames: 
            print("read %s" %filename)
            rawData = readtxt(ARTICLE_DIR+'/'+filename)
            rawData = rawData.split('\n')
            for news in rawData:
                news = news.split('。')
                for s in news:
                    d = "[\u4e00-\u9fa5]+"
                    s = re.findall(d, s)
                    sen="".join(s)
                    if len(sen)==0:
                        continue
                    sentences.append(sen)
    listSave(SENTENCE_FILE, sentences)


def gen_init():
    print("get init possibility")
    sentences = listLoad('sentences.txt')
    sen_num = len(sentences)
    init = {}

    for s in sentences:
        # start=Decode(s[0])
        start=s[0]
        init.setdefault(start, 0)
        init[start] += 1
    del init['新']
    saveJson('init.json',init)

def main():
    gen_sentences()
    # gen_init()
    # sens=listLoad('sentences.txt')
    # sens=topinyin(sens)
    # print(sens)

if __name__ == '__main__':
    main()
