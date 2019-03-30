import numpy as np


def Input(filename):
    input_data = []
    with open(filename, 'r', encoding='UTF-8') as f:
        for l in f.readlines():
            l = l.replace('\n', '')
            l = l.split(' ')
            input_data.append(l)
    return input_data

def Output(filename, data):
    with open(filename, 'w', encoding='UTF-8') as f:
        for d in data:
            f.write(d+'\n')

            
if __name__ == '__main__':
    filename = '../input.txt'
    input_data = Input(filename)
    print(input_data)
