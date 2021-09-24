#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np


# In[20]:


arr = [1,2,3,4,5,6]


# In[23]:


arr1 = np.array(arr)


# In[24]:


arr1 + arr1


# In[25]:


arr1 + 1


# In[27]:


arry = np.arange(0,25)


# In[28]:


arry


# In[32]:


arry_d = arry.reshape(5,5)


# In[33]:


arry_d.shape


# In[34]:


arry_d


# In[35]:


arry_d.sum(axis = 0)


# In[36]:


arry_d.sum(axis = 1)


# In[37]:


arry_d.sum(axis = 2)


# In[38]:


account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])  


# In[39]:


account_total = account_transactions.sum()


# In[40]:


account_total


# In[ ]:




