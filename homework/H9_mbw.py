# SESSDSA18课程上机作业
# 【H9】排序查找编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在5月25日23：59之前提交到作业提交网站

# 划重点：
#### 将本文件与一个说明分析文档共两个文件打包提交，
#### 命名为h9_学号_姓名，如h9_1700000012_张三

#
# by TYY
# 2018.5.15

# =========== 1 无切片的二分搜索 ==========
# 用递归算法实现二分搜索，避免用切片操作。

def binarySearch_noSlice(alist, item):
    
    def bs(alist,head,tail,item):
        middle = (tail + head) // 2
        if alist[middle] == item or alist[tail] == item:
            return True
        if middle == head:
            return False
        if alist[middle] > item:
            return bs(alist,head,middle,item)
        else:
            return bs(alist,middle,tail,item)

    return bs(alist,0,len(alist)-1,item)


# 检验
print(binarySearch_noSlice([1, 2, 3, 4, 5], 5))                                                     # True
print(binarySearch_noSlice([1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97], 70)) # False
print(binarySearch_noSlice([1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, 217,
       226, 235, 244, 253, 262, 271, 280, 289, 298], 233))                                          # False


# =========== 2 ADT Map =================
# 采用数据链(chaining)的冲突解决技术来实现ADT Map，
# 要求实现ADT Map中定义的所有方法：put(key, data), get(key), __delitem__(key), __len(), __contains__(key)
class Node():
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.next = None

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setData(self, newkey, newitem):
        self.key = newkey
        self.item = newitem

    def setNext(self, newnext):
        self.next = newnext

class HashMap_chaining():
            
    def __init__(self, size=11):
        self.mapSize = size
        self.dataSize = 0
        self.mapList = [None] * size

    def put(self, key, data):
        hashKey = key % self.mapSize
        newNode = Node(key,data)
        if not self.mapList[hashKey]:
            self.mapList[hashKey] = newNode
            self.dataSize += 1
        else:
            nowNode = self.mapList[hashKey]
            if nowNode.getKey() == key:
                nowNode.setData(key,data)
                return
            while nowNode.getNext():
                nowNode = nowNode.getNext()
                if nowNode.getKey() == key:
                    nowNode.setData(key,data)
                    return
            nowNode.setNext(newNode)
            self.dataSize += 1


    def get(self, key):
        hashKey = key % self.mapSize
        nowNode = self.mapList[hashKey]
        while nowNode:
            if nowNode.getKey() == key:
                return nowNode.getItem()
            else:
                nowNode = nowNode.getNext()
        print("Key",key,"not found.")
        return None

    __setitem__ = put
    __getitem__ = get

    def __delitem__(self, key):
        hashKey = key % self.mapSize
        nowNode = self.mapList[hashKey]
        if not nowNode:
            print("Key",key,"not found.")
            return False
        if nowNode.getKey() == key:
            self.mapList[hashKey] = nowNode.getNext()
            self.dataSize -= 1
            return True
        while nowNode.getNext():
            if nowNode.getNext().getKey() == key:
                nowNode.setNext(nowNode.getNext().getNext())
                self.dataSize -= 1
                return True
            nowNode = nowNode.getNext()

    def __len__(self):
        return self.dataSize

    def __contains__(self, key):
        hashKey = key % self.mapSize
        nowNode = self.mapList[hashKey]
        while nowNode:
            if nowNode.getKey() == key:
                return True
            else:
                nowNode = nowNode.getNext()
        return False

# 检验
m = HashMap_chaining()
for i in range(1, 101, 11):
    m[i] = i
print(len(m))
for i in range(1, 101, 22):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    m[i] = i * 2
for i in range(1, 101, 11):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    del m[i]
print(len(m))
for i in range(1, 101, 11):
    print(i in m, end=' ')
print('\n')

# 10
# 1 23 45 67 89
# 2 12 46 34 90 56 134 78 178 100
# 5
# False True False True False True False True False True


# =========== 3 大小自动增长的散列表 =======
# 采用开放定址冲突解决技术的散列表，课件中是固定大小的，如果希望在负载因子达到某个阈值之后，
# 散列表的大小能自动增长，该如何设计算法？
# 请写一个算法说明和分析，并实现之。
class HashTable:
    def __init__(self,size=11):
        self.size = size
        self.dataSize = 0
        self.lamb = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def updateSize(self,num = 1):
        self.dataSize += num
        #print(self.slots,self.dataSize)
        self.lamb = self.dataSize / self.size
        if self.lamb > 0.8:
            self.size += self.size + 1
            oldslots = self.slots
            olddata = self.data
            self.slots = [None] * self.size
            self.data = [None] * self.size
            self.dataSize = 0
            for i in range(self.size//2):
                if oldslots[i] != None:
                    self[oldslots[i]] =olddata[i]
            self.lamb = self.dataSize / self.size

    def hashfunction(self,key):
        return key % self.size

    def rehash(self,oldhash,skip = 1):
        return (oldhash + skip) % self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.updateSize()
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                skip = 1
                nextslot = self.rehash(hashvalue,skip)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    if skip > self.size:
                        nextslot = self.rehash(nextslot)
                    else:
                        skip += 2
                        nextslot = self.rehash(nextslot,skip)
                    #print(self.slots)
                    #print(nextslot,self.slots[nextslot])
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                    self.updateSize()
                else:
                    self.data[nextslot] = data

    def get(self,key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        skip = 1
        while not found and not stop: #and self.slots[position] != None:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                if skip > self.size:
                    position = self.rehash(position)
                    if position == startslot:#是否会陷入死循环？
                        stop = True
                else:
                    position = self.rehash(position,skip)
                    skip += 2
                    startslot = position
        return data

    __setitem__ = put
    __getitem__ = get

    def __delitem__(self, key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        skip = 1
        while not found and not stop: #and self.slots[position] != None:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None
                self.updateSize(-1)
            else:
                if skip > self.size:
                    position = self.rehash(position)
                    if position == startslot:#是否会陷入死循环？
                        stop = True
                else:
                    position = self.rehash(position,skip)
                    skip += 2
                    startslot = position
        return found

    def __len__(self):
        return self.dataSize

    def __contains__(self, key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        skip = 1
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,skip)
                skip += 2
                if position == startslot:#是否会陷入死循环？
                    stop = True
        return found

# 检验
m = HashTable()
for i in range(1, 101, 11):
    m[i] = i
print(len(m))
for i in range(1, 101, 22):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    m[i] = i * 2
for i in range(1, 101, 11):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    del m[i]
print(len(m))
for i in range(1, 101, 11):
    print(i in m, end=' ')
print('\n',m.slots)

# 10
# 1 23 45 67 89
# 2 12 46 34 90 56 134 78 178 100
# 5
# False True False True False True False True False True


# =========== 4 取“中值”快排 ==============
# 自行设计一种取“中值”的方法实现快速排序，并与课件中的快速排序比较性能。
# 请写一个算法说明和分析，并实现之。
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
    return alist

def partition(alist,first,last):
    #pivotvalue = alist[first]
    middle = (last+first)//2
    alist[first],alist[middle]=alist[middle],alist[first]
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# 检验
l1=[54,26,93,17,77,31,44,55,20]
quickSort(l1)
print(l1)