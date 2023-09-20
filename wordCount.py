#! usr/bin/env python3

import sys
import os
import re

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

wordCount = {}
for word in re.findall(r'\w+', inputFile.read()):
    word = word.lower()
    if word not in wordCount:
        wordCount[word] = 0 
    wordCount[word] += 1


for i in sorted(wordCount):
    outputFile.write(f"{i} {wordCount[i]}\n")