#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas-profiling


# In[2]:


pip install seaborn


# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas_profiling import ProfileReport


# In[29]:


data=pd.read_csv("SampleSuperstore.csv")


# In[30]:


data.head()


# In[31]:


data.shape


# In[32]:


data.count().isnull()


# In[33]:


data.dtypes


# In[34]:


data.describe(include="all")


# In[35]:


data.isna().sum()


# In[36]:


data.columns


# In[37]:


sns.relplot(x='Sales', y='Category', hue='State', data=data)
plt.show()


# In[59]:



plt.figure(figsize=(40,25))
sns.scatterplot(x="State", y="Profit", data=data);
plt.show()


# In[57]:


plt.figure(figsize=(40,25))
sns.scatterplot(x="Sub-Category", y="Profit", data=data);
plt.show()


# In[39]:


correlation=data.corr()
correlation


# In[40]:


sns.heatmap(correlation)


# In[41]:


data['Sales'].hist(bins=25)


# In[42]:


data['Profit'].hist(bins=25)


# In[43]:


data['State'].hist(bins=25)


# In[44]:


data['Category'].hist(bins=25)


# In[45]:


data['Segment'].hist(bins=25)


# In[46]:



print(data.boxplot(column='Sales'))


# In[47]:



print(data.boxplot(column='Profit'))


# In[48]:


data.boxplot(column='Profit', by = 'Category')


# In[56]:


plt.figure(figsize=(40,25))
data.boxplot(column='Profit', by = 'State')


# In[50]:


sns.countplot(data.Category)


# In[51]:


sns.countplot(data.Segment)


# In[52]:


plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=data)
plt.show()


# In[53]:


plt.figure(figsize=(40,25))
sns.barplot(x=data['Sub-Category'], y=data['Profit'])


# In[60]:


plt.figure(figsize = (10,4))
sns.lineplot('Discount', 'Profit', data = data, color = 'r', label= 'Discount')
plt.legend()


# In[61]:


data.groupby("State").Profit.agg(["sum","mean","min","max"])


# In[ ]:




