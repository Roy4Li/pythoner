# try... except...
file_name = 'sum.py'
try:
	f = open(file_name,'r')
	print 'file open'
	f.close()
except:
	print 'file not exist'
print 'done'