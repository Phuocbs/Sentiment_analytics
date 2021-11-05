#!/usr/bin/env python
# coding: utf-8

# In[27]:


from selenium import webdriver
import time


# In[28]:


browser = webdriver.Chrome("/Users/phuph/OneDrive\Máy tính/chrome/chromedriver")


# In[29]:


browser.get("https://steamcommunity.com/app/883710/positivereviews/?browsefilter=toprated&snr=1_5_100010_")


# In[32]:


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# In[33]:


new_height


# In[34]:


last_height


# In[45]:


SCROLL_PAUSE_TIME = 3
last_height = browser.execute_script("return document.body.scrollHeight")
new_height = browser.execute_script("return document.body.scrollHeight")

while True:
    last_height = new_height
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break


# In[55]:


recomend=browser.find_elements_by_class_name("title")
reco=[item.text for item in recomend]


# In[49]:


len(reco)


# In[104]:


name=browser.find_elements_by_class_name("apphub_friend_block")
na=[item.text for item in name]


# In[85]:


len(na)


# In[54]:


review=browser.find_elements_by_class_name("apphub_CardTextContent")
rev=[item.text for item in review]


# In[59]:


import pandas as pd


# In[61]:


df=pd.DataFrame()


# In[129]:


df["Name"]=x


# In[70]:


df["Review"]=rev


# In[67]:


df["Recommend"]=reco


# In[72]:


df["Posted"]=posted


# In[130]:


df


# In[82]:


posted=[]
for i in range (0,len(rev)):
  date=rev[i].split("\n")[0]
  x=date
  rev[i]=rev[i].replace(x,"")
  date=date.replace("Posted:", "")
  posted.append(date)


# In[116]:


ne=df["Name"]


# In[127]:


x=[]
for i in range (0,len(ne)):
    x.append(ne[i].split("\n")[0])


# In[134]:


for i in range (0,len(ne)):
    ne[i]=ne[i].split("\n")[0]


# In[135]:


ne


# In[136]:


df.to_csv(r'C:\Users\phuph\OneDrive\Máy tính\Thunhapdulieu\gamenotrecommend.csv')


# In[ ]:




