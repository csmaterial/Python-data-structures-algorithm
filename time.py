import time
def sum(n):
	start = time.time()
	theSum = 0
	for i in range(1,n+1):
		theSum +=i
	end = time.time()
	return theSum,end - start

for i in range(5):
	print("the sum is %d required %10.7f seconds" % sum(1000000))
