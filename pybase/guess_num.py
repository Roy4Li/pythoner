# guess num
def is_equal(a,b):
	if a > b:
		print 'too big'
		return False
	elif a < b:
		print 'too small'
		return False
	else:
		print 'Bingo!'
		return True
		
from random import randint
num = randint(1,1000)
print 'I\'ve picked a num from 1 to 1000',
print 'you can guess'
ans = 0
i = 0
while not is_equal(ans,num):
	ans = input()
	if '' == ans:
		print 'input error'
		continue
print 'you are too clever'


		
	




raw_input()