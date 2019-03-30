from loadfile import load_pinyin
from loadfile import load_character
from random import randint
import math

pinyin_dict = load_pinyin()
# dict_file='NoOne.pkl'
# character_couter = load_character(dict_file)
one_couter=load_character('one2.pkl')       
two_couter=load_character('two.pkl')
three_couter=load_character('three.pkl')
four_couter=load_character('four.pkl')
couters=[one_couter,two_couter,three_couter,four_couter]

def get_random(word_size):
    ran = []
    size=word_size
    while word_size:
        i = randint(1,4)
        ran.append(i)
        word_size -= i
        if word_size<0:
            word_size=size
            ran=[]
    return ran


def dfs(n, words, words_p, str):
    num = len(words)
    if n == 0:
        # score = character_couter[str]
        try:
            score = couters[num-1][str]
        except Exception as e:
            score=0
        words_p[str] = score
        return
    for w in words[num-n]:
        str += w
        dfs(n-1, words, words_p, str)
        str=str[:-1]


def get_word(words):
    num = len(words)
    words_p = {}
    dfs(num, words, words_p, "")
    # print(words_p)
    str = max(words_p, key=words_p.get)
    score=words_p[str]
    threhold=2
    fail=(score<threhold)
    return (str, words_p[str],fail)


def prep(input_data):
    word_size = len(input_data)
    # brute force
    p = {}  # all possibility
    word = []
    rans = set()
    for i in range(word_size):
        characters = pinyin_dict[input_data[i]]
        word.append(characters)
    total=100
    for i in range(int(total)):
        if i%5==0:
            print("progress : %d / %d" %(i,total))
        ran = get_random(word_size)
        if tuple(ran) in rans:
            continue
        rans.add(tuple(ran))

        strs = ""
        scores = 0
        beg = 0
        fail=False
        for j in ran:
            (str, score,fail) = get_word(word[beg:j+beg])
            if fail:
                break
            strs += str
            if j==1:
                score//=20
            # print(score*pow(j,j*2))
            scores += score*pow(j,j*2)
            beg += j
        if fail:
            continue
        try:
            if p[strs]<scores:
                p[strs] = scores
        except Exception as e:
            p[strs] = scores



    res_str = max(p, key=p.get)
    res_score = p[res_str]

    return (res_str, res_score)
if __name__ == '__main__':
    print(character_couter)