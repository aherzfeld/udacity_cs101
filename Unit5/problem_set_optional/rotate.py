# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

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

def rotate(s, n):
    p = make_alphabet()
    result = ''
    for c in s:
    	if c in p:
    		c = shift_n_letters(c, n)
    	result = result + c
    return result

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
