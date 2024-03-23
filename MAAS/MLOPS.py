#!/usr/bin/env python
# coding: utf-8

# ### MLOPS Makine öğrenme modelleri geliştirme,dağıtma ve yönetme işlemleri
# 

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv('hiring.csv')
df.head()


# In[3]:


import seaborn as sns
sns.countplot(x='experience',data=df)


# In[4]:


d={'two':2,'three':3,'five':5,'seven':7,'ten':10,'eleven':11}
df.experience=df.experience.map(d)
df


# In[5]:


df.isnull().sum()


# In[6]:


df['experience']=df.experience.fillna(0)


# In[7]:


df.isnull().sum()


# In[8]:


df['test_score']=df.test_score.fillna(df.test_score.median)


# In[9]:


df.isnull().sum()


# In[10]:


y=df['salary']
X=df.drop('salary',axis=1)


# In[11]:


from sklearn.linear_model import LinearRegression
import pickle # dosya kaydetme ve acma
import warnings
warnings.filterwarnings('ignore')


# In[12]:


df.head()


# In[14]:


lr=LinearRegression()
lr.fit(X,y)
pickle.dump(x,open('model.pkl','wb'))


# In[ ]:


pip install pickle


# In[ ]:




