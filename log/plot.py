# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:18:21 2020

@author: USER
"""

import matplotlib.pyplot as plt

f = open(r'20200619-085203.log')
content = f.readlines()
f.close()


reward = []
eva = []

for i in range(len(content)):
    a = content[i].split(',')
    if len(a)== 5:
        if a[3][1] == 'r':
            b = int(a[3][-2]+a[3][-1])
            reward.append(b)
        if a[4][2] == 'v':
            c = int(a[4][-2]+a[4][-1])
            eva.append(c)
            
plt.plot(reward)
plt.plot(eva)
    