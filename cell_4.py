#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def SimpleAdding(num):
  i = 0
  for x in range(num,0,-1):
    i =  i + x
  return i
num = 1
while True:
  num = int(input("please enter number between 1 to 1000: "))
  if num >= 1 and num <= 1000:
    break
print (SimpleAdding(num))

