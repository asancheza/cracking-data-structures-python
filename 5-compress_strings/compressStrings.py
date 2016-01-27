# -*- coding: utf-8 -*-
#!/usr/bin/python

def compressString(string):
	word = list(string)
	newstring = []

	last = word[0]
	count = 0

	for i in range(len(string)):
		if string[i] == last:
			count = count + 1
		else:
			newstring.append(last + str(count))
			last = string[i]
			count = 1

	newstring.append(last + str(count))
	
	return newstring

print compressString('aabbbccc')