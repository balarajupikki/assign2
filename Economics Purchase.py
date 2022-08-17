#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
ecom=pd.read_csv("Ecommerce Purchases.csv.csv")


# ecom

# In[3]:


ecom


# In[4]:


ecom.head()


# In[5]:


ecom.info()


# In[6]:


ecom["Purchase Price"].mean()


# In[7]:


ecom['Purchase Price'].max()


# In[8]:


ecom['Purchase Price'].min()


# In[9]:


ecom[ecom['Language']=='en'].count()


# In[10]:


ecom[ecom['Job'] == 'Lawyer'].info()


# In[11]:


ecom['AM or PM'].value_counts()


# In[12]:


ecom['Job'].value_counts().head(5)


# In[13]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# In[14]:


ecom[ecom["Credit Card"] == 4926535242672853]['Email']


# In[15]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# In[16]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# In[17]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


# In[ ]:




