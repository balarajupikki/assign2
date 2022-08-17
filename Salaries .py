#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


sal=pd.read_csv("Salaries1.csv.csv")


# In[5]:


sal


# In[6]:


sal.head()


# In[7]:


sal.info()


# In[8]:


sal['OvertimePay'].max()


# In[9]:


sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]


# In[10]:


sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"]


# In[11]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()]


# In[12]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()]


# In[13]:


sal.groupby("Year").mean("BasePay")


# In[14]:


sal['JobTitle'].nunique()


# In[15]:


g=sal.groupby("JobTitle").count()
top5=g.sort_values(by='Id',ascending=False)[:5]
top5['Id']


# In[16]:


cd_sal = sal[sal['Year'] == 2013]
grp = cd_sal.groupby('JobTitle').count()
count = grp[group['Id'] == 1]
count.count()['Id']


# In[17]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# In[18]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# In[19]:


sal['t-len'] = sal['JobTitle'].apply(len)

sal[['t-len', 'TotalPayBenefits']].corr()


# In[ ]:




