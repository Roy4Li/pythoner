# and-or usage
a = 'hell'
b = 'heaven'
c = True and a or b
print c

a = ''
c = True and a or b
print c 
print (True and [a] or [b])[0]