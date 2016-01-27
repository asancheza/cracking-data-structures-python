# -*- coding: utf-8 -*-
#!/usr/bin/python

def permutationString(stringA, stringB):
	if len(stringA) != len(stringB):
		return False

	if ''.join(sorted(stringA)) == ''.join(sorted(stringB)):
		return True

	return False

print permutationString('dog ', 'dog')