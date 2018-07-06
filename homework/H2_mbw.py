'''
SESSDSA18课程上机作业
【H2】Python入门编程

说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
（1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
上交作业时提交本文件，命名为h2_学号_姓名.py，如h2_1700000012_张三.py
（2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
（3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
（4）作业在3月16日 23：59之前提交到教学网


by TYY
2018.3.9
'''



'''
======= 1 字符移动 =======
创建一个函数，接受一个字符串和一个正整数n作为参数，
返回把原字符串字符位置向右移动n个字符的字符串。
例如：
** 接受的参数是"abcd"和1，返回的字符串是"dabc"；
** 接受的参数是"mnbol"和2，返回的字符串是"olmnb"。
'''
def reverse(s, n):
    result = ""
    # 请在此写下你的代码
    slen=len(s)
    n=n%slen # 为了不越界以及考虑到负数的情况
    result=s[slen-n:]+s[:slen-n] # 前后移位即可
    # 代码结束
    return result

# 调用检验
print("1-reverse", reverse("abcd", 1))
print("1-reverse", reverse("mnbol", 2))
# print("1-reverse", reverse("mnbol", -7))

'''
======= 2 阶乘求和 =======
创建一个函数，接受一个正整数n作为参数，返回s=1!+2!+3!+……+n!的值。
例如：
** 接受的参数是3，返回的数是9；
** 接受的参数是6，返回的数是873。
'''
def factorailSum(n):
    s = 0
    # 请在此写下你的代码
    if n > 1:
        temp = 1
        for i in range(1,n+1): # 计算n！
            temp = temp * i
        s = temp + factorailSum(n-1) # 递归求和
    elif n >=0:
        s = 1
    else:
        print('error input, input must > 0, your input is %d.' % n) # n不能小于0
    # 代码结束
    return s

# 调用检验
print("2-factorailSum", factorailSum(3))
print("2-factorailSum", factorailSum(6))
# print("2-factorailSum", factorailSum(-6))


'''
======= 3 数字转换 =======
创建一个函数，接受一个英文字符串作为参数，返回该字符串的整数表示。
例如：
** 接受的参数是"eight-nine"，返回的是89；
** 接受的参数是"one-two-three-four-five"，返回的是12345。
'''
def transNum(s):
    n = 0
    # 请在此写下你的代码
    numDic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    slist = s.split('-') # 先分割为字符串列表
    numStr=''
    for num in slist:
    	numStr = numStr + numDic[num.lower()] # 无视大小写
    n=int(numStr) # 先将数字作为字符串相加，最后再转换为整数，省去了进位的麻烦
    # 代码结束
    return n

# 调用检验
print("3-transNum", transNum("eight-nine"))
print("3-transNum", transNum("one-two-three-four-five"))
# print("3-transNum", transNum("one-two-three-four-fIVe"))


'''
======= 4 创建字典 =======
创建一个函数，接受两个长度相同的元组，
用这两个元组中的所有数据组成一个字典并返回。
例如：
** 接受的参数是(1, 2, 3)和("abc", "def", "ghi")，返回{1:"abc", 2:"def", 3:"ghi"}。
'''
def createDict(keys, values):
    d = dict()
    # 请在此写下你的代码
    if len(keys)!=len(values):
        print('length do not match.') # 数目不相等时
    else:
        d = {keys[i]:values[i] for i in range(len(keys))}
    # 代码结束
    return d

# 调用检验
print("4-creatDict", createDict((1,2,3), ("abc","def","ghi")))
# print("4-creatDict", createDict((1,2,3), ("abc","def",)))


'''
======= 5 创建集合 =======
创建一个函数，接受两个字符串作为参数，返回两个字符串字符集合的并集。
例如：
** 接受的参数为"abc"和"bcd"，返回set(['a', 'b', 'c', 'd'])。
'''
def createSet(s1, s2):
    union = set()
    # 请在此写下你的代码
    union=set(s1)|set(s2)
    union=sorted(union)
    # 代码结束
    return union

# 调用检验
print("5-creatSet", createSet("abc", "bcd"))


'''
======= 6 月份天数 =======
创建一个函数，接受两个参数y和m，分别表示年和月，返回此年此月的天数。
（如大月有31天，小月有30天，而闰年的2月有29天，平年则只有28天，
年份如果能被4整除但不能被100整除或者能被400整除为闰年）
例如：
** 接受的参数为2018和2，返回28
** 接受的参数为2015和7，返回31
'''
def countDays(y, m):
    day = 0
    # 请在此写下你的代码
    if m in [1,3,5,7,8,10,12]: # 大月
        day = 31
    elif m in [4,6,9,11]: # 小月
        day = 30
    elif m == 2: # 2月
        if y%400==0 or (y%4==0 and y%100!=0): # 判断闰年
            day = 29
        else:
            day = 28 
    else:
        print('Unexpected input.')
    # 代码结束
    return day

# 调用检验
print("6-countDays", countDays(2018, 2))
print("6-countDays", countDays(2015, 7))
# print("6-countDays", countDays(2015, 14))


'''
======= 7 判断水仙花数 =======
创建一个函数，接受一个参数n(n>=100)，判断这个数是否为水仙花数，
返回True或者False。（即满足如果这个数为m位数，
则每个位上的数字的m次幂之和等于它本身。）
例如：
** 接受参数为153，返回True（1^3 + 5^3+ 3^3 = 153）
** 接受参数为282，返回False
'''
def isNarcNum(n):
    flag = False
    # 请在此写下你的代码
    nlist = list(str(n)) # 把整数转化成一个包含每一位的列表
    mul = len(nlist) # 识别位数
    flag = n==sum(int(x)**mul for x in nlist)
    # 代码结束
    return flag

# 调用检验
print("7-isNarcNum", isNarcNum(153))
print("7-isNarcNum", isNarcNum(282))
# print("7-isNarcNum", isNarcNum(1634))


'''
======= 8 杨辉三角 =======
创建一个函数，接受一个参数n，返回n阶杨辉三角。
例如：
** 接受参数为6，返回：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''
def printTri(n):
    s = ""
    # 请在此写下你的代码
    for i in range(n): # 对于三角中的每一行
        if i == 0:
            rowList = [1] # 初始化第一行的值
            s += '1'
        else:
            rowList = [sum(i) for i in zip([0]+rowList,rowList+[0])] # 把第i行的值更新为第i+1行的值
            s += '\n1'
            for i in rowList[1:]: # 将该行的值加入到字符串s中
                s += ' ' + str(i)
    return s

# 调用检验
print("8-printTri", printTri(6))


'''
======= 9 判断质数 =======
对于大于1的数，如果除了1和它本身，它不能再被其它正整数整除，
那么我们说它是一个质数。创建一个函数，接受一个参数n，判断它是否是质数。
例如：
** 接受参数为18，返回False
** 接受参数为31，返回True
'''
def isPrime(n):
    flag = False
    # 请在此写下你的代码
    flag = not True in {n%x == 0 for x in range(2,int(n**0.5)+1+1)} # 计算n能否被从2到n的开方向上取整的那个数之间的任何一个数整除
    # 代码结束
    return flag

# 调用检验
print("9-isPrime", isPrime(18))
print("9-isPrime", isPrime(31))


'''
======= 10 水仙花数 =======
创建一个函数，接受一个参数max(max>=1000)，调用另一题编写的判断函数，
求100到max之间的水仙花数，返回一个包含换行符的字符串，
每个数作为一行输出（每一个数之后有一个换行符'\n'，包括最后一个数）
例如：
** 接受参数为2333，返回：
153
370
371
407
1634
'''
def printNarcNum(n):
    s = ""
    # 请在此写下你的代码
    if n >= 153:
        s = '153'
        for i in range(154,n+1):
            if isNarcNum(i):
                s += '\n' + str(i)
    # 代码结束
    return s

# 调用检验
print("10-printNarcNum", printNarcNum(2333))
#print("10-printNarcNum", printNarcNum(152))

