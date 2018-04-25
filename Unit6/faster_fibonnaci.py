#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
	n1 = 1
	n0 = 0
	fib = 1
	i = 1
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		while i < n:
			fib = n1 + n0
			n0 = n1
			n1 = fib
			i = i + 1
		return fib

print fibonacci(5)


print fibonacci(36)
#>>> 14930352