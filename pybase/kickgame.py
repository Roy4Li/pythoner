# kick game
from random import choice
def in_list(ele,list):
	for i in list:
		if ele == i:
			break
	return i
	
direction = ['left','right','center']
print 'choose a direction to kick the ball'
print 'left,right,or center'
yours = raw_input()
while yours != in_list(yours,direction):
	print 'wrong input,try again:left,right,or center'
	yours = raw_input()
print 'All right,you\'ve chosen %s' %(yours)
keepers = choice(direction)
print 'The keeper\'s choose is %s' %(keepers)
if (yours == keepers):
	print 'Sorry,you lost the goal'
else:
	print 'Good,you got the goal'
