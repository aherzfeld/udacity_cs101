# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def make_alphabet():
	p = []
	i = 0
	while len(p) < 26:
		p.append(chr(ord('a') + i))
		i = i + 1
	return p

def shift_n_letters(letter, n):
	p = make_alphabet()
	from_start = 0
	if p.index(letter) + n <= 25:
		return p[p.index(letter) + n]
	from_start = n - (26 - p.index(letter))
	return p[from_start]
	



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
