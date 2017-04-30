from timeit import Timer
def test1():
	l = []
	for i in range(1000):
		l.append(i)

t1 = Timer("test1()","from __main__ import test1")
print "concat %f seconds \n" % t1.timeit(number = 1000)
'''
首先创建一个timer对象，需要两个参数，第一个是需要反复运行的语句，第二个是为了建立运行环境而只需要运行一次的“安装语句”

然后调用这个对象的timeit方法，其中可以指定反复运行多少次，计时完毕后返回以秒为单位的时间。

'''
