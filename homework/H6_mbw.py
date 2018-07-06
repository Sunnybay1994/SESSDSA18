# SESSDSA18课程上机作业
# 【H6】线性表与链式存储结构编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h6_学号_姓名.py，如h6_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月10日23：59之前提交到教学网
#
#
# by TYY&ZHD
# 2018.4.2


class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

# ======== 1 UnorderedList ========
# 用链表实现UnorderedList的如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 选做：UnorderedList(iterable) -> new UnorderedList initialized from iterable's items
# 选做：__eq__, __iter__
class UnorderedList():
    def __init__(self, argv=None):
        self.head = None
        self.lsize = 0
        if argv != None:
            for item in argv:
                self.append(item)

    def isEmpty(self):
        #return self.head.getNext() == None
        return self.lsize == 0

    def add(self, item):
        newNode = Node(item)
        if self.lsize == 0:
            self.head = newNode
        else:
            firstNode = self.head
            newNode.setNext(firstNode)
            self.head = newNode
        self.lsize += 1
        return self
    
    def search(self, item):
        nowNode = self.head
        result = False
        while nowNode != None:
            if nowNode.getData() == item:
                result = True
                break
            nowNode = nowNode.getNext()
        return result

    def size(self):
        return self.lsize

    def remove(self, item):
        if self.lsize == 0:
            raise Exception('List is empty.')
        if self.head.getData() == item:
            self.head = self.head.getNext()
            self.lsize -= 1
            return True
        else:
            prevNode = self.head
            nowNode = self.head.getNext()
            while nowNode != None:
                if nowNode.getData() == item:
                    prevNode.setNext(nowNode.getNext())
                    self.lsize -= 1
                    return True
                prevNode = nowNode
                nowNode = nowNode.getNext()
        return False

    def append(self, item):
        newNode = Node(item)
        if self.lsize == 0:
            self.head = newNode
        else:
            nowNode = self.head
            while nowNode.getNext() != None:
                nowNode = nowNode.getNext()
            nowNode.setNext(newNode) 
        self.lsize += 1
        return self

    # 搜索value，从下标start到stop，左闭右开
    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = self.size()
        nowNode = self.head
        for i in range(0,stop):
            if i < start:
                continue
            elif nowNode.getData() == value:
                result = i
                break
            nowNode = nowNode.getNext()
        if nowNode == None:  #如果没找到，返回一个errer
            raise Exception('Value not found.')
        return result

    def pop(self, pos=-1):
        if pos < 0:
            pos = self.lsize + pos
        if  pos >= self.lsize or pos < 0:
            raise IndexError('list index out of range')
        if pos == 0:
            result = self.head.getData()
            self.head = self.head.getNext()
            self.lsize -= 1
            return result
        prevNode = None
        nowNode = self.head
        for i in range(0, pos):
            prevNode = nowNode
            nowNode = nowNode.getNext()
        result = nowNode.getData()
        prevNode.setNext(nowNode.getNext())
        self.lsize -= 1
        return result

    def insert(self, pos, item):
        if pos < 0 or pos > self.lsize:
            raise IndexError('list index out of range')
        elif pos == 0:
            add(self,item)
        elif pos == self.lsize:
            append(self, item)
        else:
            #上面两个条件确保了插入的位置在首尾之间
            newNode = Node(item)
            prevNode = self.head
            for i in range(0, pos-1):   #将nowNode指向目标位置的前一个位置
                prevNode = prevNode.getNext()
            newNode.setNext(prevNode.getNext())
            prevNode.setNext(newNode)
        self.lsize += 1
        return self

    def __len__(self):
        return self.lsize

    def __str__(self):
        return repr([self[i] for i in range(0, self.lsize)])

    __repr__ = __str__

    def __getitem__(self, argv):
        #请参考：http://gis4g.pku.edu.cn/python3-slice-getitem/
        #可以不用处理负数
        if isinstance(argv, int):
            pos = argv
            if pos < 0 or pos >= self.lsize:
                raise IndexError('list index out of range')
            nowNode = self.head
            for i in range(0, pos):
                nowNode = nowNode.getNext()
            return nowNode.getData()
        
        elif isinstance(argv, slice):
            start = argv.start
            stop = argv.stop
            step = argv.step
            reverse = False
            if start == None:
                start = 0
            if stop == None:
                stop = self.lsize
            if step == None:
                step = 1
            if step < 0:
                reverse = True
                if start == None:
                    start = self.lsize - 1
                if stop == None:
                    stop = -1
                start, stop = stop + 1, start + 1
                step = - step
            index = range(start, stop, step)    #记录哪些序号是需要输出的
            result = []
            nowNode = self.head
            for i in range(0, stop):
                if i in index:
                    result.append(nowNode.getData())
                nowNode = nowNode.getNext()
            if reverse:
                result.reverse()
        return result

    def __eq__(self, other):
        if not isinstance(other, UnorderedList):
            print(123)
            return False
        elif self.size() != other.size():
            return False
        else:
            myNode = self.head
            yourNode = other.head
            while myNode != None:
                if myNode.getData() != yourNode.getData():
                    return False
                myNode = myNode.getNext()
                yourNode = yourNode.getNext()
        return True

    def __iter__(self):
        return [self[i] for i in range(0, self.lsize)].__iter__()

# 检验
print("======== 1 UnorderedList ========")
mylist = UnorderedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.isEmpty())           # False
print(mylist.search(5))           # False
print(mylist.size())              # 10
print(mylist.index(2))            # 2
print(mylist.pop())               # 18
print(mylist.pop(2))              # 2
print(mylist)                     # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))                # 9
print(mylist[4])                  # 8
print(mylist[3:8:2])              # ['10', 10, 14]
yourlist = UnorderedList([3, 0, 4, '10', 8, 10, 12, 14, 16])
print(mylist==yourlist)
for item in yourlist:
    print(item)




# ======== 2 OrderedList ========
# 将OrderedList作为UnorderedList的子类来实现
# 实现ADT OrderedList的所有接口:
# add, remove, search, isEmpty, size, index, pop
# 注：不继承insert, append方法
class OrderedList(UnorderedList):
    def insert(self, pos, item):
        raise AttributeError("'OrderedList' object has no attribute 'insert'")

    def append(self, item):
        raise AttributeError("'OrderedList' object has no attribute 'append'")

    def add(self, item):
        newNode = Node(item)
        if self.lsize == 0:
            self.head = newNode
        elif self.head.getData() > item:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            nowNode = self.head
            while nowNode.getNext() != None and nowNode.getNext().getData() <= item:  #寻找插在哪个节点后面
                nowNode = nowNode.getNext()
            newNode.setNext(nowNode.getNext())
            nowNode.setNext(newNode)
        self.lsize += 1

# 检验
print("======== 2 OrderedList ========")
mylist = OrderedList()
for i in range(0, 10, 2):
    mylist.add(i)
mylist.add(3)
mylist.remove(6)
mylist.add(5)
print(mylist.isEmpty())         # False
print(mylist.search(8))         # True
print(mylist)                   # [0, 2, 3, 4, 5, 8]
print(mylist.pop())             # 8
print(mylist.size())            # 5
print(mylist.index(4))          # 3
print(mylist.pop(-2))           # 4
print(mylist[1:])               # [2, 3, 5]



# ======== 3 ADT Stack & Queue ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class Stack():
    def __init__(self):
        self.items = UnorderedList()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def peek(self):
        return self.items[self.items.size()-1]

class Queue():
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()


# 检验
print("======== 3 ADT Stack & Queue ========")
s = Stack()
q = Queue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())      # 9 0
print(s.pop(), q.size())          # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())      # 0 False



# ======== 4 DoublyLinkedList ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量，引用列表中最后一个节点
# 增加getTail方法
class DoublyLinkedList():
    def __init__(self, argv=None):
        self.head = None
        self.tail = None
        self.lsize = 0
        if argv != None:
            for item in argv:
                self.add(item)

    def getTail(self):
        return self.tail

    def isEmpty(self):
        #return self.head.getNext() == None
        return self.lsize == 0

    def add(self, item):
        newNode = Node(item)
        if self.lsize == 0:
            self.head = newNode
            self.tail = newNode
        else:
            firstNode = self.head
            newNode.setNext(firstNode)
            firstNode.setPrev(newNode)
            self.head = newNode
        self.lsize += 1
    
    def search(self, item):
        nowNode = self.head
        result = False
        while nowNode != None:
            if nowNode.getData() == item:
                result = True
                break
            nowNode = nowNode.getNext()
        return result

    def size(self):
        return self.lsize

    def remove(self, item):
        nowNode = self.head
        result = False
        while nowNode != None:
            if nowNode.getData() == item:
                prevNode = nowNode.getPrev()
                nextNode = nowNode.getNext()
                if prevNode != None:
                    prevNode.setNext(nextNode)
                else:
                    self.head = nowNode
                if nextNode != None:
                    nextNode.setPrev(prevNode)
                else:
                    self.tail = nowNode
                result = True
                self.lsize -= 1
                break
            nowNode = nowNode.getNext()
        return result

    def append(self, item):
        newNode = Node(item)
        if self.lsize == 0:
            self.head = newNode
            self.tail = newNode
        else:
            lastNode = self.tail
            newNode.setPrev(lastNode)
            lastNode.setNext(newNode)
            self.tail = newNode
        self.lsize += 1

    # 搜索value，从下标start到stop，左闭右开
    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = self.size()
        nowNode = self.head
        for i in range(0,stop):
            if i < start:
                continue
            elif nowNode.getData() == value:
                result = i
                break
            nowNode = nowNode.getNext()
        if nowNode == None:  #如果没找到，返回一个errer
            raise Exception('Value not found.')
        return result

    def pop(self, pos=-1):
        if pos < 0:
            if  pos < -self.lsize:
                raise IndexError('list index out of range')
            nowNode = self.tail
            for i in range(1, -pos):
                nowNode = nowNode.getPrev()
        else:
            if  pos >= self.lsize:
                raise IndexError('list index out of range')
            nowNode = self.head
            for i in range(0, pos):
                nowNode = nowNode.getNext()
        result = nowNode.getData()
        prevNode = nowNode.getPrev()
        nextNode = nowNode.getNext()
        if prevNode != None:
            prevNode.setNext(nextNode)
        else:
            self.head = nowNode
        if nextNode != None:
            nextNode.setPrev(prevNode)
        else:
            self.tail = nowNode
        self.lsize -= 1
        return result

    def insert(self, pos, item):
        if pos < 0 or pos > self.lsize:
            raise IndexError('list index out of range')
        elif pos == self.lsize:
            append(self, item)
        else:
            #上面两个条件确保了插入的位置必定是个已有数据的位置
            newNode = Node(item)
            if self.lsize == 0:     #空链表直接加入
                self.head = newNode
                self.tail = newNode
            nowNode = self.head
            for i in range(0,pos):  #将nowNode指向目标位置
                nowNode = nowNode.getNext()
            prevNode = nowNode.getPrev()
            if prevNode != None:
                prevNode.setNext(newNode)
                newNode.setPrev(prevNode)
            else:
                self.head = newNode
            newNode.setNext(nowNode)
            nowNode.setPrev(newNode)
        self.lsize += 1
        return item

    def __len__(self):
        return self.lsize

    def __str__(self):
        return repr([self[i] for i in range(0, self.lsize)])

    __repr__ = __str__

    def __getitem__(self, argv):
        #请参考：http://gis4g.pku.edu.cn/python3-slice-getitem/
        #可以不用处理负数
        if isinstance(argv, int):
            pos = argv
            if pos < 0 or pos >= self.lsize:
                raise IndexError('list index out of range')
            nowNode = self.head
            for i in range(0, pos):
                nowNode = nowNode.getNext()
            return nowNode.getData()
        
        elif isinstance(argv, slice):
            start = argv.start
            stop = argv.stop
            step = argv.step
            reverse = False
            if start == None:
                start = 0
            if stop == None:
                stop = self.lsize
            if step == None:
                step = 1
            if step < 0:
                reverse = True
                if start == None:
                    start = self.lsize - 1
                if stop == None:
                    stop = -1
                start, stop = stop + 1, start + 1
                step = - step
            index = range(start, stop, step)    #记录哪些序号是需要输出的
            result = []
            nowNode = self.head
            for i in range(0, stop):
                if i in index:
                    result.append(nowNode.getData())
                nowNode = nowNode.getNext()
            if reverse:
                result.reverse()
        return result

# 检验
print("======== 4 DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())   # 16
print(mylist.isEmpty())                       # False
print(mylist.search(5))                       # False
print(mylist.size())                          # 10
print(mylist.index(2))                        # 2
print(mylist.pop())                           # 18
print(mylist.pop(2))                          # 2
print(mylist)                                 # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))                            # 9
print(mylist[4])                              # 8
print(mylist[3:8:2])                          # ['10', 10, 14]
