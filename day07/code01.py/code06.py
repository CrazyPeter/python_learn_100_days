# _*_ coding: utf-8 _*_

import random

all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = ''
for _ in range(1,5):
    index = random.randint(0,len(all_chars)-1)
    code+=all_chars[index]
print(code)

