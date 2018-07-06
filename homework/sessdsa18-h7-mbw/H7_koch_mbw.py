# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写Koch曲线代码
# 使用海龟制图，画出Koch曲线
# 可直接绘制5阶曲线，阶数n可以调整
#
# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6

import turtle

def drawKochKurve(t, length, n = 1):
	r = 1
	if n <= 6:
		r = 1 - 0.16 * n
	if n % 3 == 0:
		c = (r, 1, 1)
	elif n % 3 == 1:
		c = (1, r, 1)
	elif n % 3 == 2:
		c = (1, 1, r)
	oriC = t.fillcolor()
	t.fillcolor(c)

	leng = length / 3
	if n == 1:
		t.begin_fill()
		t.fd(leng)
		t.lt(60)
		t.fd(leng)
		t.rt(120)
		t.fd(leng)
		t.lt(60)
		t.bk(leng)
		t.fd(leng*2)
		t.end_fill()
	else:
		drawKochKurve(t, leng, n - 1)
		#tc用于上色
		tc=turtle.Turtle()
		tc.pu()
		tc.setpos(t.pos())
		tc.seth(t.heading())
		tc.fillcolor(c)
		tc.speed(t.speed())
		tc.pd()
		tc.ht()
		tc.begin_fill()
		tc.lt(60)
		tc.fd(leng)
		tc.rt(120)
		tc.fd(leng)
		tc.lt(60)
		tc.bk(leng)
		tc.end_fill()
		
		t.lt(60)
		drawKochKurve(t, leng, n - 1)
		t.rt(120)
		drawKochKurve(t, leng, n - 1)
		t.lt(60)
		drawKochKurve(t, leng, n - 1)
	t.fillcolor(oriC)
	


def KochCurve(n):
	t=turtle.Turtle()
	w=turtle.Screen()
	t.pu()
	t.setpos(-300, -100)
	t.fillcolor((1,1,1))
	t.pd()
	turtle.tracer(0)
	t.speed(0)
	drawKochKurve(t, 600, n )
	turtle.update()
	w.exitonclick()

# 测试
KochCurve(6)