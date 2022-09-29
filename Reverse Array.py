#!/usr/bin/env python
# coding: utf-8

# In[4]:


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 

A = [9, 2, 8, 4, 5, 7]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[ ]:




