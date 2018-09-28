# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:31:02 2018

@author: adriano.santin
"""

# operator auxilia na ordenacao das listas
import operator

logfile = open ('log.txt', 'r') 
url = {}
rescode = {}

for line in logfile:
    # Pega somente as linhas do log que interessam: 
    # no formato level=info response_body="" request_to"<url>" response_headers=  response_status="<code>"
    if line.startswith('level=info'):
        
        # Quebra as linhas em arrays e pega as informacoes necessarias: a url e o code
        # Em seguida os guarda em um dictonary que conta o número de ocorrencias de cada url e code
        sp = line.split('"')
        if sp[3] in url:
            url[sp[3]] += 1
        else:
            url[sp[3]] = 1
        
        if sp[5] in rescode:
            rescode[sp[5]] += 1
        else:
            rescode[sp[5]] = 1
            
# Ordena as urls por quantidade de ocorrencias de forma decrescente e ordena os codes pelos codigos de forma crescente
sorted_url = sorted(url.items(), key=operator.itemgetter(1), reverse=True)
sorted_res = sorted(rescode.items(), key=operator.itemgetter(0))

# Imprime os tres maiores urls em quantidade e a tabela com os codes e quantidades 
for i in range(3):
    print str(sorted_url[i][0]) + ' - ' + str(sorted_url[i][1])
print('\n')
for r in sorted_res:
    print str(r[0]) + ' - ' + str(r[1])
