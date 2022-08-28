#!/usr/bin/env python
# coding: utf-8

# In[10]:


def sample_string(s):
    d = {"UPPER CASE":0, "LOWER CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER CASE"]+=1
        elif c.islower():
             d["LOWER CASE"]+=1
        else:
            pass
    print("No. of Upper case letters are : ",d["UPPER CASE"])
    print("No. of lower case letters are : ",d["LOWER CASE"])
    
sample_string('The quick Brow Fox')    


# In[ ]:




