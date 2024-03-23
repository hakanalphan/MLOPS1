#!/usr/bin/env python
# coding: utf-8

# pip install streamlit 

# In[2]:


import streamlit as st
import pandas as pd
import pickle


# In[3]:


st.title('maaş tahmin sistemi:heavy_dollar_sign:')


# In[8]:


model=pickle.load(open("model.pkl","rb"))
tecrube=st.number_input("Tecrube",1,10)
yazili=st.number_imput('Sınav',1,10)
mulakat=st.number_input('Mulakat',1,10)
if st.button("Tahmin Et"):
        tahmin=model.predict([[tecrube.yazili,mülakat]])
        tahmin=round(tahmin[0],2)
        st.write("f Tahmin edilen maas:{tahmin}")


# In[ ]:




