#!/usr/bin/env python
# coding: utf-8

# In[96]:


#ffmc tick
#dc tick
#dmc tick
#isi tick
#api for weather details
#coordinates of west-singhbham tick
#ML applied on dataset
#use it on calculated value
#make script to regularly update the details
# return json
# part 2
# heatmap from nasa 
# or cluster from cal data
# use cluster coordinates on our forest
# or use common sense / general research


# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


import pandas as pd
import math


# In[ ]:





# In[ ]:





# In[98]:
glom=0

def ffmc(T,H,W,fo=85):
    mo= 205.2*(101-fo)/(82.9+fo)
    Ed= (0.942*H)**0.679 + 11*math.exp((H-100)/10)+0.18*(21.1-T)*(1-math.exp(-0.115*H))
    if mo>Ed:
        ka=0.424*(1-(H/100)**1.7) + (0.0684*W**0.5)*(1-(H/100)**8)
        kd=0.0579*ka*(math.exp(0.0365*T))
        m=Ed+((mo-Ed)*(math.exp(-2.303*kd)))
    if mo<Ed:
        Ew= (0.618*H)**0.753 + 10*math.exp((H-100)/10)+0.18*(21.1-T)*(1-math.exp(-0.115*H))
        if mo<Ew:
            kb=0.424*(1-((100-H)/100)**1.7)+(0.0664*(W**0.5))*(1-((100-H)/100)**8)
            kw=0.0579*kb*(math.exp(0.0365*T))
            m=Ew-((Ew-mo)*(math.exp(-2.303*kw)))
        if mo==Ed or mo==Ew:
            m=mo
        if Ed>mo>Ew:
            m=mo
    glom=m
    F=(82.9*(250-m))
    F=F/(205.2+m)
    return F
    
    
    
    
    


# In[99]:


def dmc(R,Po,H,T,Month):
    if R>1.5:
        re=0.92*R -1.27
    else:
        re=R
    Mo=20+math.exp(5.6348-(Po/43.43))
    if Po<=33:
        b=100/(0.5+0.3*Po)
    if Po<=65:
        b=14-1.3*math.log(Po)
    else:
        b=6.2*math.log(po*17.2)
    Mr=Mo+((1000*re)/(48.77+b*re))
    Pr=244.72-43.43*(math.log(Mr-20))
    Le=[6.5,7.5,9.0,12.8,13.9,13.9,12.4,10.9,9.4,8.0,7.0,6.0]
    K=1.894*(T+1.1)*(100-H)*Le[Month]*(10**(-6))
    P=Po+100*K
    return P


# In[100]:


def dc(R,Do,month,T):
    if R>2.8:
        rd=0.83*R-1.27
    else:
        rd=R
    Qo=800*math.exp(Do/400)
    Qr=Qo+3.937*rd
    Dr=400*math.log(800/Qr)
    lf=[-1.6,-1.6,-1.6,0.9,3.8,5.8,6.4,5.0,2.4,0.4,-1.6,-1.6]
    V=0.36*(T+2.8)+lf[month]
    D=Do+0.5*V
    return D


# In[ ]:





# In[101]:


def ISI(T,H,W,fo=85):
    fw=math.exp(0.05039*W)
    fmc=ffmc(T,H,W,fo)
    m=20725-(205.2*fmc)
    m=m/(fmc+82.9)
    ff=91.9*math.exp(-0.1386*m)*(1+(m**5.31)/((4.93)*(10**7)))
    R=0.208*fw*ff
    return R


# In[ ]:





# In[93]:


#rest taken by json


# In[94]:


# data prepared


# In[ ]:




