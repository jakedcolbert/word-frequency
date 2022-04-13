#!/usr/bin/env python
#
#

# Iterate through file and keep count of each word occurance

import sys

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def countKeywords():
	dict = {}
	with open(sys.argv[1],'r') as file:
		for line in file: # each line
			for word in line.split(): # each word
				for c in word: # each character
					if c in punc: # remove string punctuation
						word = word.replace(c, "")
				# find keyword occurances
				if word in dict.keys():
					dict[word] += 1
				else:
					dict[word] = 1

	# print keywords and count
	dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
	for key, value in dict:
		print(key, " : ", value)
	
if __name__ == "__main__":
	countKeywords()
