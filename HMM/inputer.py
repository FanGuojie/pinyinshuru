import numpy as np
def Input(filename):
    input_data=[]
    with open(filename,'r') as f:
        for l in f.readlines():
            l=l.replace('\n','')
            l=l.split(' ')
            input_data.append(l)

    return input_data
if __name__ == '__main__':
    filename='../input.txt'
    input_data=Input(filename)
    print(input_data)