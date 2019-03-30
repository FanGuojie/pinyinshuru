import pypinyin
import sys


def loadstd(filename):
	res = []
	with open(filename, 'r', encoding='utf-8') as f:
		for l in f.readlines():
			l=l.replace('\n','')
			res.append(l)
	return res


def savetxt(filename, data):
	with open(filename, 'w') as f:
		for d in data:
			str=""
			for p in d:
				str+=p+" "
			f.write(str.strip()+'\n')


def main():
	data = loadstd('t.txt')
	pinyin = []
	for l in data:
		p = pypinyin.lazy_pinyin(l)
		pinyin.append(p)
	savetxt('t_in.txt', pinyin)


if __name__ == '__main__':
	main()
