# -*- coding: utf-8 -*-
#!/usr/bin/python

def reverseString(string):
	word = list(string)

	for i in range(len(word) / 2):
		tmp = word[i]
		word[i] = word[len(word) - i - 1]
		word[len(word) - i - 1] = tmp

	return word

print reverseString('alex')