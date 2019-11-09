#!/usr/bin/env python
# coding: utf-8

# In[150]:


import utils


# In[151]:


import pandas as pd
import json


# In[152]:


with open('yash.json') as f:
    js = json.load(f)


# In[153]:


T=js[1]['temperatureHigh']
W=js[0]['windSpeed']
H=js[2]['humidity']
R=js[3]['precipIntensityMax']


# In[154]:


with open('output.json') as f:
    js1 = json.load(f)


# In[ ]:





# In[155]:


try:
    with open('pre.json') as f:
        js2 = json.load(f)
    Po=js2['Po']
    Do=js2['Do']
    fo=js2['Fo']
except:
    Po=15
    Do=33
    fo=85


# In[ ]:





# In[ ]:





# In[156]:


x=[]
for i in range(1,10):
    for j in range(1,10):
        x.append(j)


# In[157]:


y=[]
for i in range(1,10):
    for j in range(1,10):
        y.append(i)


# In[158]:


temp=[]
for i in range(0,81):
    temp.append(js1[i][1]['temperatureHigh'])
humid=[]
for i in range(0,81):
    humid.append(js1[i][2]['humidity'])
Rain=[]
for i in range(0,81):
    Rain.append(js1[i][3]['precipIntensityMax'])
wind=[]
for i in range(0,81):
    wind.append(js1[i][0]['windSpeed'])


    


# In[159]:


T=temp[0]
W=wind[0]
R=Rain[0]
H=humid[0]
ff=utils.ffmc(T,H,W)
dm=utils.dmc(R,Po,H,T,10)
dro=utils.dc(R,Do,10,T)
IS=utils.ISI(T,H,W,fo)


# In[160]:


from datetime import datetime
data={'X':y,'Y':x,'month':'aug','day': datetime.today().strftime('%a').lower(),'FFMC':ff,'DMC':dm,'DC':dro,'ISI':IS,'temp':T,'RH':H,'wind':W,'rain':R}


# In[161]:


set_=pd.DataFrame(data)


# In[162]:


set_['area']=float(0)


# In[163]:


set_.to_csv('adder.csv',index=None)


# In[164]:


data={'Do':dro,'Fo':ff,'Po':dm}
with open('pre.json','w') as f:
    json.dump(data,f)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




