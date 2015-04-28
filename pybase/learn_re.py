# find cellphone num and name
import re

def find_cellphone(s):
	m = re.findall(r'\b1[0-9]{10}\b',s)
	if [] == m:
		return
	print m
def find_name(s):
	m = re.findall(r'\b[A-Z]\S*?\b',s)
	if [] == m:
		return
	print m
def find_fixed(s):
	m = re.findall(r'\(0\d{2,3}\)\d{7,8}\b|\b0\d{2,3}[- ]?\d{7,8}\b',s)
	if [] == m:
		return
	print s
	print m

file_name = raw_input('input file_name\n')

try:
	f = file(file_name,'r')
except :
	print 'open file error!\n'
lines = f.readlines()
for i in lines:
	find_cellphone(i)
	find_name(i)
	find_fixed(i)

