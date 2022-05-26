#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


import chromedriver_autoinstaller as chromedriver
chromedriver.install()


# In[3]:


import pandas as pd


# In[4]:


executable_path = {'executable_path': chromedriver.install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[6]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


slide_elem.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# Mars Facts

# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[18]:


df.to_html()


# In[19]:


browser.quit()


# In[ ]:





# In[ ]:




