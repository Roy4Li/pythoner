# added sum 

def sum(start,end):
	i = 0
	while end >= start:
		i += end
		end -= 1
	return i

print sum(1,100)