#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[34]:


dataset = pd.read_csv("loan.csv")
dataset.head(5)


# In[37]:


dataset.shape


# In[39]:


((614-480)/614)*100


# In[25]:


dataset.isnull().sum()


# In[30]:


sns.heatmap(dataset.isnull())
plt.show()


# In[31]:


dataset.drop(columns=["Credit_History"],inplace=True)


# In[36]:


dataset.dropna(inplace = True)


# In[ ]:





# In[ ]:





# In[ ]:




