# -*- coding: utf-8 -*-
import csv
import sys
import os
from collections import defaultdict


#dict = {}
listRow = []
reader = csv.reader(open("train.csv", "rb"))
#reader = csv.reader(f)
for row in reader:
	listRow.append(list(reversed(row)))
	#print list(reversed(row))
 
f.close()
#print listRow
dict = defaultdict(list)
for k, v in listRow:
	dict[k].append(v)

print dict
print len(dict['angry'])
print len(dict['neutral'])
print len(dict['sad'])
print len(dict['happy'])


