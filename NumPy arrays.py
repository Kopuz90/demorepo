#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


my_list = [1,2,3,4]


# In[6]:


type(my_list)


# In[7]:


np.array(my_list)


# In[8]:


myarry = np.array(my_list)


# In[9]:


myarry


# In[10]:


type(myarry)


# In[11]:


my_matrix =[[1,2,3],[4,5,6],[7,8,9]]


# In[12]:


np.array(my_matrix)


# In[13]:


my_matrix


# In[16]:


mymtrix = np.array(my_matrix)


# In[17]:


mymtrix


# In[26]:


np.arange(5,40,1.5)


# In[28]:


np.zeros((5,2))


# In[29]:


np.zeros(2)


# In[30]:


np.ones((2,4))


# In[31]:


np.linspace(2,24,3)


# In[32]:


np.linspace(1,14,4)


# In[33]:


np.linspace(2,24,8)


# In[36]:


len(np.linspace(2,24,8))


# In[39]:


np.eye(4)


# In[40]:


np.eye(4,7)


# In[41]:


np.random.rand(3)


# In[96]:


a = np.random.rand(4,9)


# In[97]:


a


# In[95]:


np.random.rand(50)


# In[52]:


np.random.randn(8)


# In[63]:


np.random.randn(200)


# In[59]:


np.random.randint(2,14,(5,4))


# In[67]:


np.random.seed(20)
np.random.rand(5)


# In[68]:


np.random.rand(5)


# In[69]:


np.random.rand(5)


# In[71]:


np.random.seed(20)
np.random.rand(6)


# In[72]:


arr = np.arange(0,30)


# In[73]:


arr


# In[75]:


arr.reshape(5,6)


# In[82]:


nrarry = np.random.randint(0,100,20)


# In[86]:


nrarry


# In[87]:


nrarry.max()


# In[88]:


nrarry.min()


# In[89]:


nrarry.argmax()


# In[91]:


nrarry.argmin()


# In[90]:


sorted(nrarry)


# In[92]:


nrarry.dtype


# In[98]:


a.dtype


# In[99]:


b = np.random.rand(2,6)


# In[100]:


b


# In[101]:


b.dtype


# In[102]:


# TASK: Create a numpy array called myarray which consists of 101 evenly linearly spaced points between 0 and 10.


# In[109]:


myarray = np.linspace(0,101,10)


# In[110]:


myarray


# In[ ]:




