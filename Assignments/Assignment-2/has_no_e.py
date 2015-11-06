#hyo kim 100560568
def has_no_e(string):
	if 'e' in string:
		return False
	elif 'E' in string:
		return False
	else:
		return True
	
reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()
print(has_no_e(line))

while line != '':
	line = reader.readline()
	print(has_no_e(line))


