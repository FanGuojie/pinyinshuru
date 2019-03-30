import re
import sys
import numpy as np
import jieba
import collections
import pickle
def listLoad(filename):
    res=[]
    with open(filename,'r') as f:
        for l in f.readlines():
            res.append(l.replace('\n',''))
    return res

def savefile(filename, data):
	with open(filename, 'wb') as f:
		pickle.dump(data, f)


def loadfile(filename):
	with open(filename,'rb') as f:
		pklObj = f.read()
		data=pickle.loads(pklObj)
	return data


def getChinese():
	d = "[\u4e00-\u9fa5]+"
	ws = []
	with open('2016-11.txt', 'r') as f:
		for l in f.readlines():
			l = re.findall(d, l)
			ws.append(" ".join((l)))
	return ws


def  expandThree():
	two=loadfile("two.pkl")
	three=loadfile("three.pkl")
	for i in list(two.keys()):
		if two[i]<30:
			del two[i]

	size_two=len(two)
	three2={}
	k=0
	total=pow(size_two,2)


	for i in two:
		for j in two:
			k+=1
			if k%1000000==0:
				print("progress : %d /%d" %(k,total))
			if i[1]==j[0]:
				three2[i+j[1]]=(two[i]+two[j])//2
	print(three2)
	three2+=three
	savefile('three2.pkl',three2)

def extract_one():
	dataset=loadfile("dataset.pkl")
	for i in list(dataset.keys()):
		if len(i)>1:
		 	del dataset[i]
	one_dict={}
	j = len(dataset)
	for i in dataset.most_common():
		one_dict[i[0]] = j
		j -= 1
	# print(words.most_common)
	print(one_dict)
	savefile('one2.pkl', one_dict)
	print("extract successfully")



def one_word():
	sentences = getChinese()
	ws = []
	for s in sentences:
		for w in s:
			ws.append(w)
	words = collections.Counter(ws)
	for i in list(words.keys()):
		if words[i] < 20:
			del words[i]
	print(len(words))
	words_dict = {}
	j = len(words)
	for i in words.most_common():
		words_dict[i[0]] = j
		j -= 1
	# print(words.most_common)
	print(words_dict)
	savefile('one.pkl', words_dict)
	print("extract successfully")


def getRawPkl():
	# ws = getChinese()
	ws=listLoad('./sentences.txt')
	i = 0
	d = collections.Counter()
	s = len(ws)
	for w in ws:
		seg = jieba.cut(w, cut_all=True, HMM=True)
		d += collections.Counter(seg)
		i += 1
		if i % 1000 == 0:
			print("progress :  %d / %d" % (i, s))

	print(d)
	savefile('dataset.pkl',d)
	print('save successfully')


def handle():
	# delete one word
	two = collections.Counter()
	three = collections.Counter()
	four = collections.Counter()
	with open('dataset.pkl', 'rb') as f:
		pklObj = f.read()
		c = pickle.loads(pklObj)
		for i in list(c.keys()):
			if len(i) == 1:
				del c[i]
			elif len(i) == 2:
				two[i] = c[i]
			elif len(i) == 3:
				three[i] = c[i]
			elif len(i) == 4:
				four[i] = c[i]

	savefile("two.pkl", two)
	savefile("three.pkl", three)
	savefile("four.pkl", four)
	print("save respectively")


if __name__ == '__main__':
	getRawPkl()