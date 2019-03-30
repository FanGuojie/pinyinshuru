import pickle
import json
def load_pinyin():
    filename='./data/pinyin.json'
    with open(filename,'r',encoding='utf-8') as f:
        jsObj=f.read()
        d=json.loads(jsObj)
    return d

def load_character(filename):
    filename="./data/"+filename
    with open(filename,'rb') as f:
        pklObj=f.read()
        res=pickle.loads(pklObj)
    return res