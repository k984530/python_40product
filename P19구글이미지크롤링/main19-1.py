#!/usr/bin/env python
# coding: utf-8

# In[18]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait = 10)


# In[23]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys('바다')
elem.send_keys(Keys.RETURN)


# In[24]:


import time
elem = driver.find_element(By.TAG_NAME,'body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    
try:
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[26]:


links = []
images = driver.find_elements(By.CSS_SELECTOR,'#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print('찾은 이미지 개수 : ', len(links))


# In[27]:


import urllib.request

for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "C:\\Users\\82108\\python_40product\\P19구글이미지크롤링\\사진다운로드\\"+str(k)+'.jpg')

print('다운로드 완료하였습니다.')
    

