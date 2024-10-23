#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[3]:


pip install requests


# In[4]:


pip install beautifulsoup4


# In[5]:


pip install pandas


# In[7]:


import requests


# In[8]:


from bs4 import BeautifulSoup


# In[12]:


import pandas as pd


# In[13]:


from pymongo import MongoClient


# In[79]:


df = pd.read_csv("C:\\Users\\22103227\\Desktop\\Medical-Equipment-Suppliers.csv")
client = MongoClient('localhost',27017)
db = client['MedEquipSuppDatabase']
collection = db['Main']
collection.insert_many(df.to_dict('record'))


# In[82]:


data = list(collection.find())
ds=pd.DataFrame(data)
print(ds)


# In[84]:


data = list(collection.find("practiceaddress":"CA"))
dc=pd.DataFrame(data)
print(dc)


# In[ ]:




