#!/usr/bin/env python
# coding: utf-8

# In[24]:


num= 50
First = 0
Second = 1
           

for i in range(0, num):
   
        Next = First
        print(First,end=" ")
        First = Second
        Second = Next + Second
        if First>50:
            break


# In[ ]:




