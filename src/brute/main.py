from inouter import Input,Output
from predict import prep
from show import pre_show,post_show
import sys
if len(sys.argv)==1:
    input_file = '../input.txt'
    output_file = './test.txt'
elif len(sys.argv)==3:
    input_file = sys.argv[1]
    output_file=sys.argv[2]
input_data = Input(input_file)
input_num = len(input_data)
out=[]
for i in range(input_num):
    pre_show(i,input_data[i])
    (out_str, out_score) = prep(input_data[i])
    out.append(out_str)
    post_show(out_str,out_score)
Output(output_file,out)