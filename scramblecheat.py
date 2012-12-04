#!/usr/bin/env python

import itertools
from appscript import *
import time
import sys

words = []
f = open("words_out", 'r')
wordsI = f.read().split("\n")
for word in wordsI:
	if len(word) > 3 and len(word) <= 6:
		word = word.lower()
		words += [word]


letters = sys.argv[1]

results = []

for i in range(6,3,-1):
	for word in itertools.permutations(letters,i):
		word = ''.join(word)
		if word in words:
			print word
			if not word in results:
				results += [word]
				if i < 6:
					if 's' in letters:
						results += [word + 's']
					if 'y' in letters:
						results += [word + 'y']
				if i < 5:
					if 'e' in letters and 'd' in letters:
						results += [word + 'ed']

for word in itertools.permutations(letters,3):
	word = ''.join(word)
	results += [word]

print "results"
print results

app(u'Safari').activate()
time.sleep(1)

sleeptime = 60.0 / len(results)

for result in results:
	app(u'System Events').processes[u'Safari'].keystroke(result + "\r")
	time.sleep(sleeptime)

