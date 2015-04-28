# from time import *
import time
i = 0
for g in dir(time):
	i += 1 
	print '%s: %s' %(str(g),'')
print 'total : %d' % i

from time import *
print time()
# print dir(time)
# print time.time()
# print time.ctime()
# print time.asctime()
# print time.localtime()
# print 
