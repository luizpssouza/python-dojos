#! /usr/bin/python3
# -*- coding : utf-8 -*-

from datetime import datetime
import re

fname = 'log.txt'
contador = 0
with open(fname, 'r') as f:
    content = f.readlines()
    for i, line in enumerate(content):
        if(line.strip() == ''):
            continue
        
        valores = line.split('] -')
        valores[0] = re.sub(r'[^\w]', ' ', str(valores[0]).strip())
        valores[1] = re.sub(r'[^\w]', ' ', str(valores[1]).strip())
        
        try:
            data = datetime.strptime(str(valores[0]).strip(), '%Y %m %d %H %M %S')
        except:
            continue

        datai = data.replace(hour=10, minute=0, second=0)
        dataf = data.replace(hour=16, minute=0, second=0)
        if(data >= datai and data <= dataf and 'Abertura da Porta OK' in str(valores[1]).strip()):
            contador += 1
            print("Linha [{0}] - OK - Valores {1} ".format((i + 1), line.replace('\n','')))

print("Passaram {0} pessoas entre os horários das 10:00:00 e 16:00:00".format(contador))
