file_name = 'score_sheet.txt'
f = file(file_name,'r')
cont = f.readlines()
for line in cont:
	score = 0
	data = line.split()
	for i in data[1:]:
		score += int(i)
	print '%s: total score is %4d,average score is %3d' %(data[0],score,score/4)
f.close()
	
	