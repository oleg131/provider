#!/usr/bin/env python
# coding: utf-8

# In[49]:



import time
import pandas as pd
import json

from ping3 import ping


# In[8]:


hosts = [
    '192.168.1.254',
    '8.8.8.8'
]


# In[50]:


data = []


# In[51]:


while 1:
    res = {}
    for host in hosts:
        p = ping(host)

        print(host, p)

    res[host] = p

    res['time'] = time.time()

    time.sleep(1)

    data.append(res)

#     print(1)
    with open('data.json', 'w') as file:
        json.dump(data, file)

