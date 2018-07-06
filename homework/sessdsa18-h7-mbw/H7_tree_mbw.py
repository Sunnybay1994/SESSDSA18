# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写分形树代码，可直接运行
# 修改分形树程序，增加如下功能：
# 树枝的粗细可以变化，随着树枝缩短，也相应变细
# 树枝的颜色可以变化，当树枝非常短的时候，使之看起来像树叶的颜色
# 让树枝倾斜角度在一定范围内随机变化，如15～45度之间，左右倾斜也可不一样，做成你认为最好看的样子
# 树枝的长短也可以在一定范围内随机变化，使得整棵树看起来更加逼真

# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6

import turtle
import random
import math

# 可自行添加函数，进行有创意的改造
def drawCurve(t, length, angle):
	#画一条指定长度和弯曲角度的曲线
	if angle == 0:
		t.fd(length)
	elif length == 0:
		t.lt(angle)
	else:
		radius = length / (angle * 2 * math.pi / 360)
		if length > 0:		
			t.circle(radius,abs(angle))
		else:
			t.lt(180)
			t.circle(radius,abs(angle))
			t.lt(180)


def drawBranch(t, length, width, LorR, angle = random.randint(20,30)):
	#t代表海龟，length代表树枝的长度，width代表树枝的初始宽度，LorR代表往左偏（1）还是往右偏（-1），angle代表树枝的转角

	#调整笔的参数
	t.pencolor('#886600')
	#储存笔的初始参数
	t.width(width)
	pos = t.pos()
	heading = t.heading()

	#确定几个参数
	#通过转角和长度计算画圆的半径，并给一个向左或是向右的随机量
	angle=int(angle)
	radius = length / (angle * 2 * math.pi / 360) * LorR

	widAlpha0 = 0.3 * (150-length) / 150 + 0.6		#树的末端变细的程度
	widAlpha = pow(widAlpha0, 1 / angle)

	#开始画图
	for i in range(0,angle):
		t.circle(radius,1)
		t.width(t.width()*widAlpha)

	#递归作图
	if t.width() > 5:
		LorR = (random.randint(0, 1) * 2 - 1)
		length = length * 0.01 * random.randint(60, 90)
		drawBranch(t, length, t.width(), LorR)
		t.lt(random.randint(30,50) * -LorR)
		drawBranch(t, length, t.width() * 0.8, -LorR)
	else:
		drawTwig(t)

	#回归原始位置
	t.pu()
	t.setpos(pos)
	t.seth(heading)
	t.width(width)
	t.pd()

def drawTwig(t):
	width = t.width()
	pos = t.pos()
	heading = t.heading()

	t.width(3)
	t.pencolor('#008800')

	#坐标变换一下
	wind = 10	#风把柳叶向右吹过了一个角度
	angle = heading - 90 - wind
	if angle < 0:
		angle = 360 + angle
	if angle > 180:
		angle = angle - 360
	if angle > 0:
		angle = 180 - angle
	if angle < 0:
		angle =  -180 - angle

	#画柳枝
	miny = random.randint(-230,-180)
	while abs(angle) > 0 and t.pos()[1] > miny:
		#print(t.pencolor()[1])
		t.color((0,t.pencolor()[1]+(0.9-t.pencolor()[1])/10,0))
		drawCurve(t,random.randint(8,12),angle/2)
		angle -= angle/2
		drawLeaves(t)
	#while t.pos()[1] > miny:
	#	t.fd(10)
	#	drawLeaves(t)
	while t.pos()[1] > miny - random.randint(20,50) and abs(angle) < 3:
		drawCurve(t,random.randint(8,12),5)
		drawLeaves(t)

	#回复状态
	t.pu()
	t.width(width)
	t.setpos(pos)
	t.seth(heading)
	t.pd()

def drawLeaves(t,angle = 30):
	width=t.width()
	color = t.pencolor()
	t.width(1)
	colors = ['#66DD00','#99DD00','#00DD00']
	t.fillcolor(colors[random.randint(0,len(colors)-1)])
	t.lt(angle)
	drawLeave(t)
	t.rt(angle)
	t.rt(angle)
	drawLeave(t)
	t.lt(angle)
	t.width(width)


def drawLeave(t):
	leng = random.randint(3,6)
	t.fd(leng)
	t.pu()
	t.begin_fill()
	t.lt(30)
	t.circle(-10,60)
	t.rt(120)
	t.circle(-10,60)
	t.rt(150)
	t.end_fill()
	t.pd()
	t.bk(leng)

def drawTree():
	myWin = turtle.Screen()

	t0=turtle.Turtle()
	t0.pu()
	t0.setpos((0,-290))
	t0.seth(90)
	t0.pd()
	t0.speed(0)

	drawBranch(t0, 150, 50, 1, 5)

	myWin.exitonclick()


# 测试
drawTree()
