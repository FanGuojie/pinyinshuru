from inouter import Input,Output
from predict import prep
from show import pre_show,post_show
import sys
# output_ngram=int(input("您想尝试几元模型（2~4）"))
output_ngram=3
if len(sys.argv)==1:
    input_file = '../input.txt'
    output_file = './test.txt'
elif len(sys.argv)==3:
    input_file = sys.argv[1]
    output_file=sys.argv[2]
else:
    print(len(sys.argv))
    print("请输入 输入文件和输出文件地址，都不输入则用默认参数")
input_data = Input(input_file)
input_num = len(input_data)
for ngram in range(2,6):
    print("word %d-gram model:" %ngram)
    out=[]
    for i in range(input_num):
        pre_show(i,input_data[i])
        out_str  = prep(input_data[i],ngram)
        post_show(out_str)
        out.append(out_str)
    print("***************************************************")
    print()
    if ngram==output_ngram:
        Output(output_file,out)