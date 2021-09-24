#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


arry = np.arange(0,10)


# In[5]:


arry


# In[6]:


arry[:5]


# In[7]:


arry[:5] = 11

# python da bu işleme izin vermiyor.


# In[8]:


arry


# In[9]:


arry = np.arange(0,10)


# In[10]:


arry


# In[11]:


arry[:] = 99


# In[12]:


arry


# In[13]:


arry_2d = [[5,10,15],[20,25,30],[35,40,45]]


# In[15]:


arry_2d = np.array(arry_2d)


# In[16]:


arry_2d


# In[17]:


arry_2d[0]


# In[18]:


np.shape(arry_2d)


# In[19]:


np.shape(arry_2d)[0]


# In[20]:


arry_2d.


# In[21]:


arry_2d.array


# In[22]:


arry_2d[1]


# In[23]:


arry_2d[1,1]


# In[24]:


arry_2d[1][1] = 24


# In[25]:


arry_2d


# In[28]:


arry_2d[:2,:2]


# In[29]:


arr = np.arange(0,11)


# In[30]:


arr


# In[31]:


arr > 4


# In[32]:


narr = arr>4


# In[36]:


arr[narr]


# In[37]:


narr


# In[38]:


arr[arr>5]


# In[42]:


# TASK: Use numpy to check how many rolls were greater than 2. For example if dice_rolls=[1,2,3] then the answer is 1.
# NOTE: Many different ways to do this! Your final answer should be an integer.


# In[58]:


dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])


# In[63]:


dice_rolls
dice_rolls.dtype


# In[64]:


#ice_rolls>2


# In[66]:


dice_rolls[dice_rolls>2]


# In[67]:


len(dice_rolls)


# In[ ]:




