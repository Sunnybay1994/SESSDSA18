# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写编写递归算法，输出Pascal三角形（杨辉三角）
# pascalTriangle(numofrow)
# numofrow表示三角形有几行
# 每行的数字都是由上一行的对角线数字相加而得
# 可直接运行输出10阶三角形，阶数numofrow可以调整
#
# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6

def pascalTriangle(numofrow):
    if numofrow == 1:
    	rowlist = [1]
    else:
    	lastlist = pascalTriangle(numofrow - 1)
    	rowlist = [sum(i) for i in zip([0] + lastlist, lastlist + [0])]
    print(' '.join([str(x) for x in rowlist]))
    return rowlist

# 测试
pascalTriangle(10)
