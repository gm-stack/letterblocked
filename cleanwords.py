#!/usr/bin/env python

words = []
import os

def wordsFromFile(filename):
	global words
	f = open(filename, 'r')
	print "reading from %s" % filename
	wordsI = f.read().split("\n")
	for word in wordsI:
		if len(word) > 3 and len(word) <= 6:
			word = word.lower()
			if word not in words: # todo: this is n^2
				words += [word]
	
	print "got %i words of %i" % (len(words), len(wordsI))

wordsFromFile("/usr/share/dict/words")
dictlist = os.listdir("dicts/")
for dict in dictlist:
	wordsFromFile("dicts/" + dict)

f = open("words_out",'w')
for word in words:
	f.write(word + "\n")