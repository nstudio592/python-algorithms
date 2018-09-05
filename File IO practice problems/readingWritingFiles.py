#Open file

'''fr = open('test.txt', 'r')
print(fr.name) # <-- print name of file
print(fr.mode) # <-- print mode of the file i.e: r, w, r+ etc
fr.close()'''

with open("test.txt", "r") as f:
	'''since file was opened with context manager, it is automatically closed \
	all operations must be done WITHIN context manager'''
	'''contents = f.read() #reads ALL contents of file into memory..only good for small files'''
	
	'''contents = f.readline() #reads file one line at a time
	print(contents, end="")'''
	
	'''read entire file using a loop'''
	for line in f:
		print(line, end="")
