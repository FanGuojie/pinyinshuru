# 目录说明
*　/src
  *　源代码目录
  *　两类算法相关程序分别在两个不同的文件夹下
  *　input.txt output.txt 默认测试样例
  *　t.py共同测试程序
  *　/src/HMM
    *　隐马尔可夫模型
    *　main.py程序入口
    *　predict.py 预测的主要逻辑
    *　show.py 辅助输出控制台的相关函数
    *　inouter.py 负责输入输出文件
    *　setup.sh 交代运行需要的数据文件都有什么
    *　t.sh 运行测试代码
    *　t.txt测试样例中文，即标准答案，可以手动填写
    *　运行t.sh后自动生成t_in.txt 和 t_out.txt分别为测试样例的输入和输出
  *　/src/brute
    *　暴力词袋模型
    *　t相关文件为测试，和HMM类似
    *　各程序和HMM类似，不一一叙述
*　prehandle
  *　预处理相关文件
  *　gen_ngram.py 生成词多元模型
  *　pinyin_prehandle.py 拼音表预处理
  *　prehandle_brute.py 暴力词袋模型预处理（从源文本出发）
  *　prehandle_hmm.py 隐马尔可夫预处理（从源文本出发）
  *　transition.py 转移概率生成（由中文句子文本出发）
*　bin
  *　windows二进制可执行文件
  *　目录清晰不多赘述
  *　exe文件后不加命令行参数会使用默认参数
  *　exe文件后可加两个命令行参数，分别代表输入文件地址和输出文件地址

# 评测说明

受限于数据集大小，bin中的二进制文件只有字的多元模型，没有词的多元模型

词的多元模型在清华云盘上，准确率更高，但加载会比较久

gram3.json 913.8M 实际上是词的二元模型，即二字词

词的三元模型多次写入文件都以失败告终，

完整清华云盘下载地址：https://cloud.tsinghua.edu.cn/d/271536dcb9a44f00b3fc/

