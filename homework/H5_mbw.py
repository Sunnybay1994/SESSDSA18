# SESSDSA18课程上机作业
# 【H5】栈与队列编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h5_学号_姓名.py，如h5_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月3日23：59之前提交到教学网
#
#
# by TYY
# 2018.3.21


# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个整数，即求值的结果。（支持 + - * / ^ 五种运算）
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def calculate(s):
    # 请在此编写你的代码（可删除pass语句）
    opratorStack = Stack()	#暂存操作符
    oprandStack = Stack()	#暂存操作数
    tokenList = s.split()	#解析表达式到操作列表
    postfixTokenList = []		#存储后缀表达式
    #记录操作符优先级
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    #中缀变后缀
    negOprFlag = True 	#负号flag，True表示负号。根据上一个字符来判断是减号还是负号，上一个字符是')'或数字则为减号，其它情况为负号。
    negNumFlag = False 	#负数flag，True表示该数为负数。

    for token in tokenList:
    	if token == '(':
    		negOprFlag = True
    		opratorStack.push(token)
    	elif token == ')':
    		negOprFlag = False
    		toptoken = opratorStack.pop()
    		while toptoken != '(':
	    		postfixTokenList.append(toptoken)
    			toptoken = opratorStack.pop()
    	elif token == '-' and negOprFlag == True:
    		negNumFlag = not negNumFlag		#考虑出现负号相连
    	elif token in '^+-*/':
    		negOprFlag = True
    		while (not opratorStack.isEmpty()) and (prec[opratorStack.peek()] >= prec[token]):
    			postfixTokenList.append(opratorStack.pop())
    		opratorStack.push(token)
    	else:
    		negOprFlag = False
    		if negNumFlag == True:
    			postfixTokenList.append(-int(token))	#若负数flag为true，将负数加入列表
    			negNumFlag = False
    		else:
    			postfixTokenList.append(int(token))

    while not opratorStack.isEmpty():
   		postfixTokenList.append(opratorStack.pop())

	#求解后缀表达式
    for token in postfixTokenList:
   		if str(token) in '^+-*/':
   			oprand2 = oprandStack.pop()
   			oprand1 = oprandStack.pop()
   			if token == '+':
   				result = oprand1 + oprand2
   			elif token == '-':
   				result = oprand1 - oprand2
   			elif token == '*':
   				result = oprand1 * oprand2
   			elif token == '/':
   				result = oprand1 / oprand2
   			elif token == '^':
   				result = oprand1 ** oprand2
   			oprandStack.push(result)
   		else:
   			oprandStack.push(token)

    result = oprandStack.pop()
    if result % 1 == 0:
    	result = int(result)

    return result
    # 代码结束

# 调用检验
print("1-calculate")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))


# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def radix_sort(s):
    # 请在此编写你的代码（可删除pass语句）
    mainQueue = Queue()
    mainQueue.items = s
    #直接建一个包含10个队列的列表
    myQue=[1,2,3,4,5,6,7,8,9,0]
    for i in range(10):
    	myQue[i] = Queue()

    flag = True 	#判断循环是否结束的标识
    sig1 = 10			
    sig2 = 1		#这两个数用于辅助取某一位上的数
    
    while True:
    	while not mainQueue.isEmpty():
    		num = mainQueue.dequeue()
    		ind = num % sig1 // sig2	#取出该数位上的数的数值直接作为队列列表索引
    		myQue[ind].enqueue(num)
    	
    	#结束判断语句块，假如上一次分组后序列1~9全空，flag置为False
    	flag = False
    	for i in range(1,10):
    		if not myQue[i].isEmpty():
    			flag = True
    			break	#有一个不为空则直接结束判断
		
		#分组合并
    	for i in range(10):
    		while not myQue[i].isEmpty():
    			mainQueue.enqueue(myQue[i].dequeue())

    	#结束循环
    	if flag == False:
    		break

    	#更新位数
    	sig1 *= 10
    	sig2 *= 10

    result = mainQueue.items
    result.reverse()

    return result
    # 代码结束

# 调用检验
print("2-sort")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))


# ======= 3 HTML =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False

def HTMLMatch(s):
    # 请在此编写你的代码（可删除pass语句）
    tagsStack = Stack()	#储存开标记的栈
    tagQueue = Queue()	#储存标记内容的队列
    flag1 = 0 			#用于判断是文本还是标记，0表示是文本，1表示是标记
    flag2 = 0 			#用于判断是开标记还是闭标记，0表示是开标记，1表示是闭标记
    result= True
    for c in s:
    	if flag1 == 0:		#如果现在不是一个标记
    		if c == '<':	#判断是否要开始一个标记
    			flag1 = 1
    			tagQueue = Queue()
    	elif c == '/':		#开始一个闭标记
    		flag2 = 1
    		#判断此时是否有未匹配的开标记
    		if tagsStack.isEmpty():
    			result = False
    			break
    		else:
    			tagQueue = tagsStack.pop()
    	elif c == '>':		#标记结束
    		#判断结束的是一个开标记还是一个闭标记
    		if flag2 == 0:	#开标记结束后压栈
    			tagsStack.push(tagQueue)
    		else:			#对于闭标记，检查闭标记和开标记是否匹配
    			if not tagQueue.isEmpty():
    				result = False
    				break
    		flag1 = 0
    		flag2 = 0
    	elif flag2 == 0:
    		tagQueue.enqueue(c)
    	elif flag2 == 1:
    		if not tagQueue.dequeue() == c:
    			result = False
    			break
    	else:	#万一有没想到的情况
    		print(c)
    	#print(tagQueue.items)

    if not tagsStack.isEmpty():
    	result = False
    return result
    # 代码结束

# 调用检验
print("3-HTMLMatch")
print(HTMLMatch("<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"))
print(HTMLMatch("<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"))

# ======= 4 击鼓传花 =======
# 将热土豆问题的模拟程序，修改为模拟"击鼓传花"，
# 即每次传递数不是常量值，而是一个随机数。
#
# 创建一个函数，接受一个参数，为一个人名列表，
# 返回经过击鼓传花后最后一个人的的人名。

def Game(namelist):
    # 请在此编写你的代码（可删除pass语句）
    pass
    # 代码结束

# 调用检验
print("4-Game")
print(Game(['Lily', 'Monica', 'Alex', 'Luke', 'Jay', 'Rachel', 'Jack']))