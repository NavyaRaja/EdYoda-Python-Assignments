#!/usr/bin/env python
# coding: utf-8

# In[6]:


def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)

s = "1234abcd"

print("The reverse string of the given string is : ",reverse(s))


# In[ ]:




