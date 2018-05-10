# -*- coding: utf-8 -*-
import csv
import sys
import os
from collections import defaultdict


#dict = {}
listRow = []
f = open(sys.argv[1], 'rb')
reader = csv.reader(f)
for row in reader:
	#listRow.append(list(reversed(row)))
	tempList = []
	tempList.append(row[-1])
	tempList.append(row[0])
	listRow.append(tempList)
	#print list(reversed(row))
 
f.close()
#print listRow
dict = defaultdict(list)
for k, v in listRow:
	dict[k].append(v.strip("'"))

print dict.keys()
for i in dict.keys():
	print len(dict[i])
	for j in dict[i]:
		oldPath = j
		newPath = i + "/" + j
		oldPath = sys.argv[2] + "/"  + oldPath
		newPath = sys.argv[2] + "/" + newPath 
		print oldPath
		print newPath
		if (os.path.isfile(oldPath)):
			os.rename(oldPath, newPath)
