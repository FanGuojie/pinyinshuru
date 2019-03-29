from inputer import Input
from predict import prep
from show import pre_show,post_show
input_file = '../input.txt'
input_data = Input(input_file)
input_num = len(input_data)
output_file = 'test.txt'
for i in range(input_num):
    pre_show(i,input_data[i])
    (out_str, out_score) = prep(input_data[i])
    post_show(out_str,out_score)
