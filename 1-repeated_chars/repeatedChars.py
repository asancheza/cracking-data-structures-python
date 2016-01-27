# -*- coding: utf-8 -*-
#!/usr/bin/python

word = 'murcielago de cojones mas largos que otra cosa'

def isRepeatedChars(string):
	dict = {}

	for char in string:
		if dict.has_key(char):
			return False
		
		dict[char]="1"

	return True

print isRepeatedChars(word)