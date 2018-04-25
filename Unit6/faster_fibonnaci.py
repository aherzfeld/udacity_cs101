#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
	current = 0
	next = 1
	for i in range(0,n):
	    current, after = after, current + after
	return current

print fibonacci(5)


print fibonacci(36)
#>>> 14930352