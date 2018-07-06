# SESSDSA18课程上机作业
# 【H8】动态规划编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h8_学号_姓名.py，如h8_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月27日23：59之前提交到作业提交网站
#
#
# by TYY&ZHD
# 2018.4.9
# last edit: 2018.4.19


# =========== 1 博物馆大盗问题 ===========
# 给定一个宝物列表treasureList = [{'w': 2,'v': 3}, {'w': 3,'v': 4}, ...] 
# 这样treasureList[0]['w']就是第一件宝物的重量，等等
# 给定包裹最多承重maxWeight > 0
# 实现一个函数，根据以上条件得到最高总价值以及对应的宝物
# 参数：宝物列表treasureList，背包最大承重maxWeight
# 返回值：最大总价值maxValue，选取的宝物列表choosenList(格式同treasureList)
def dpMuseumThief(treasureList, maxWeight):
    maxValue = 0
    choosenList = []

    # 在这里补充你的代码
    [weightList, valueList] = zip(*[[item['w'],item['v']]  for item in treasureList])
    treasureNum = len(treasureList)
    values = [[0 for j in range(maxWeight + 1)] for i in range(treasureNum + 1)]	#初始化所拿物品价值的动规表
    treasureTaked = [[[] for j in range(maxWeight + 1)] for i in range(treasureNum + 1)] 	#初始化所拿物品列表
    for i in range(1, treasureNum + 1):		#对每个物品
    	#print(i)
    	for w in range(1, maxWeight + 1):	#对每个容量
    		if w >= weightList[i - 1]:
    			newValue = values[i - 1][w - weightList[i - 1]] + valueList[i - 1]
    			if newValue > values[i - 1][w]:
    				values[i][w] = newValue 
    				treasureTaked[i][w] = treasureTaked[i-1][w - weightList[i - 1]] + [treasureList[i - 1]]
    				continue
    		values[i][w] = values[i-1][w]
    		treasureTaked[i][w] = treasureTaked[i-1][w]
    		#print(w,values[i][w],treasureTaked[i][w])
    
    maxValue = values[treasureNum][maxWeight]
    choosenList = treasureTaked[treasureNum][maxWeight]

    return maxValue, choosenList

# 检验
print("=========== 1 博物馆大盗问题 ============")
treasureList = [[{'w':2, 'v':3}, {'w':3, 'v':4}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]]
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':4, 'v':5}, {'w':4, 'v':6}, {'w':4, 'v':7}, {'w':5, 'v':7},
                     {'w':5, 'v':8}, {'w':6, 'v':8}, {'w':6, 'v':10}, {'w':7, 'v':10}, {'w':7, 'v':12}, {'w':8, 'v':12}, {'w':8, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':16}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':6}, {'w':4, 'v':7},
                     {'w':5, 'v':7}, {'w':5, 'v':8}, {'w':6, 'v':8}, {'w':6, 'v':10}, {'w':7, 'v':11}, {'w':7, 'v':12}, {'w':8, 'v':13},
                     {'w':8, 'v':14}, {'w':9, 'v':15}, {'w':9, 'v':16}, {'w':9, 'v':17}, {'w':10, 'v':17}, {'w':10, 'v':18}, {'w':11, 'v':18}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':5}, {'w':4, 'v':6},
                     {'w':5, 'v':6}, {'w':5, 'v':7}, {'w':6, 'v':8}, {'w':6, 'v':9}, {'w':7, 'v':10}, {'w':7, 'v':11}, {'w':8, 'v':12},
                     {'w':8, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':15}, {'w':9, 'v':16}, {'w':10, 'v':16}, {'w':10, 'v':17}, {'w':11, 'v':18},
                     {'w': 12, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':5}, {'w':4, 'v':6},
                     {'w':5, 'v':6}, {'w':5, 'v':7}, {'w':6, 'v':8}, {'w':6, 'v':9}, {'w':7, 'v':9}, {'w':7, 'v':10}, {'w':8, 'v':11},
                     {'w':8, 'v':12}, {'w':9, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':15}, {'w':10, 'v':16}, {'w':10, 'v':17}, {'w':11, 'v':18},
                     {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22},
                     {'w': 14, 'v': 23}, {'w': 15, 'v': 24},{'w': 15, 'v': 25}, {'w': 16, 'v': 26},{'w': 17, 'v': 27}, {'w': 18, 'v': 28}])
maxWeightList = [20, 50, 80, 100, 150]
for i in range(len(treasureList)):
    maxValue, choosenList = dpMuseumThief(treasureList[i], maxWeightList[i])
    print(maxValue)
    print(choosenList)

# 可有多种取法，以下只给出一种符合条件的宝物列表
# 29
# [{'w':2, 'v':3}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]
# 83
# [{'w': 1, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12}, {'w': 8, 'v': 13}, {'w': 9, 'v': 16}]
# 139
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18}]
# 164
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 8, 'v': 13}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 21}, {'w': 14, 'v': 22}]
# 246
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 9, 'v': 15}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27}]


# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可
def dpWordEdit(original, target, oplist):
    score = 0
    operations = []

    # 在这里补充你的代码
    oriNum = len(original)	# 原始字符串长度
    tarNum = len(target)	# 目标字符串长度
    # 记录每一步操作的分数
    scoreMat = [[0 for j in range(tarNum + 1)] for i in range(oriNum + 1)]
    # 记录每一步操作的步骤
    operationMat = [[[] for j in range(tarNum + 1)] for i in range(oriNum + 1)]
    # 初始化目标字符为空的情况
    for i in range(1, oriNum + 1):
    	scoreMat[i][0] = i * oplist['delete']
    	operationMat[i][0] = operationMat[i - 1][0] + ['delete ' + original[i - 1]]
    # 初始化原始字符为空的情况
    for j in range(1, tarNum + 1):
    	scoreMat[0][j] = j * oplist['insert']
    	operationMat[0][j] = operationMat[0][j - 1] + ['insert ' + target[j - 1]]
    for i in range(1, oriNum + 1):
    	for j in range(1, tarNum + 1):
    		# 先判断是删除还是添加
    		if scoreMat[i - 1][j] < scoreMat[i][j - 1]:
    			operationMat[i][j] = operationMat[i - 1][j] + ['delete ' + original[i - 1]]
    			scoreMat[i][j] = scoreMat[i - 1][j] + oplist['delete']
    		else:
    			operationMat[i][j] = operationMat[i][j - 1] + ['insert ' + target[j - 1]]
    			scoreMat[i][j] = scoreMat[i][j - 1] + oplist['insert']
    		# 判断复制会不会效果更好
    		if original[i - 1] == target[j - 1] and scoreMat[i - 1][j - 1] + 5 < scoreMat[i][j]:
    			scoreMat[i][j] = scoreMat[i - 1][j - 1] + oplist['copy']
    			operationMat[i][j] = operationMat[i - 1][j - 1] + ['copy ' + original[i - 1]]

    score = scoreMat[oriNum][tarNum]
    operations = operationMat[oriNum][tarNum]

    return score, operations

    return score, operations

# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy':10, 'delete':25, 'insert':20}
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]
for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)

# 操作所对应的分数可调整
# oplist = {'copy':5, 'delete':20, 'insert':20}
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':5, 'delete':10, 'insert':15}
# 45
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 45
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 125
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 135
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 130
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 145
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 150
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':10, 'delete':25, 'insert':20}
# 90
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 85
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 230
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 230
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 245
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 265
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 280
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
