# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:31:02 2018

@author: adriano.santin
"""

import operator

logfile = open ('log.txt', 'r') 
url = {}
rescode = {}

for line in logfile:
    if line.startswith('level=info'):
        sp = line.split('"')
        if sp[3] in url:
            url[sp[3]] += 1
        else:
            url[sp[3]] = 1
        
        if sp[5] in rescode:
            rescode[sp[5]] += 1
        else:
            rescode[sp[5]] = 1
            
sorted_url = sorted(url.items(), key=operator.itemgetter(1), reverse=True)
sorted_res = sorted(rescode.items(), key=operator.itemgetter(0))
for i in range(3):
    print (sorted_url[i][0], '-', sorted_url[i][1])
print('\n')
for r in sorted_res:
    print (r[0], '-', r[1])
    
input()