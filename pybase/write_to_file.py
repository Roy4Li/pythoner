# write a sentence to file
print 'input the file name:'
file_name = raw_input()
f = file(file_name,'w')
print 'type what you want to write to the file'
con = raw_input()
f.write(con)
f.close()
