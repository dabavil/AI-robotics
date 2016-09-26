

'''
return n-th number in the Fibonacci sequence

Recursive algo performance (in seconds):
n=30 : 0.2
n=33 : 1.0
n=36 : 3.7
n=39 : 15.9

Dynamic programming algo performance (in seconds):
n=30 : 0.0
n=33 : 0.0
n=36 : 0.0
n=39 : 0.0
n=100 : 0.0
n=500 : 0.0

'''

def fib(n):
	
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)


def dp_fib(n):
	if n in lib.keys():
		return lib[n]
	else :
		a = dp_fib(n-1) + dp_fib(n-2)
		lib[n] = a
		#print(lib)
		return a



lib = {1:1, 2:1}
print dp_fib(500)