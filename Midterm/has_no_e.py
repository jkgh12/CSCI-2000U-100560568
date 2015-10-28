#hyo kim 100560568 Question 6.

def has_no_e(string):
	count = 0
	while count < len(string):
		if(string[count] == 'e'):
			return False
		else:
			return True
		count+=1

reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()
print(has_no_e(line))

while line != '':
	line = reader.readline()
	print(has_no_e(line))
	
		
