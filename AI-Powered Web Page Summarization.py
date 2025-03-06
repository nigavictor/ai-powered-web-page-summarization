#!/usr/bin/env python
# coding: utf-8

# # Web Page Summarization: Harnessing the Power of AI
# #### *- Victor Niga*
# ## Introduction
# 
# This Jupyter Notebook demonstrates how to summarize web pages using the DeepSeek API(and ChatGPT API). The code fetches the content of a web page, cleans it up, and then uses the DeepSeek API to generate a summary. The notebook also includes a comparison with a similar approach using the OpenAI API, which is commented out for reference.
# 
# ## Prerequisites
# Before running this notebook, ensure you have the following:
# 
# 1. Python 3.x installed.
# 2. Required Python libraries: requests, beautifulsoup4, python-dotenv, IPython, and deepseek.
# 3. A .env file with your DeepSeek API key.
# 
# ## Installation
# To install the required libraries, run the following command:

# In[ ]:


# pip install requests beautifulsoup4 python-dotenv IPython deepseek


# ## Imports
# First, we need to import the necessary libraries. These include libraries for handling HTTP requests, parsing HTML, loading environment variables, and interacting with the DeepSeek API.

# In[13]:


# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
from deepseek import DeepSeekAPI 
import deepseek.api as api  # Import the api submodule


# ## Loading Environment Variables
# We load the environment variables from a .env file. This file should contain your DeepSeek API key.

# In[14]:


# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('DEEPOSEEK_API_KEY')

# api_key = os.getenv('OPENAI_API_KEY')


# ## Checking the API Key
# We perform a few checks to ensure the API key is correctly set up.

# In[ ]:


# Check the key
if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


# ## Initializing the DeepSeek API
# We initialize the DeepSeek API with the API key.

# In[15]:


deepseek = DeepSeekAPI(api_key)

# openai = OpenAI()


# ## Defining the Website Class
# We define a Website class to represent a web page. This class fetches the web page content, cleans it up, and extracts the title and main text.

# In[20]:


# Some websites need you to use proper headers when fetching them:
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)


# ## Summarizing the Web Page
# We define a function summarize that uses the DeepSeek API to generate a summary of the web page. A similar approach using the OpenAI API is commented out for reference.

# In[29]:


# # And now: call the deepseek API. 

def summarize(url):
    website = Website(url)
    response = deepseek.chat_completion(
        model="deepseek-chat",  # Replace with the actual model name if different
        messages=messages_for(website)
    )
    return response

# # And now: call the OpenAI API. 

# def summarize(url):
#     website = Website(url)
#     response = openai.chat.completions.create(
#         model = "gpt-4o-mini",
#         messages = messages_for(website)
#     )
#     return response.choices[0].message.content


# ## Displaying the Summary
# We define a function display_summary to display the summary in a Jupyter Notebook using Markdown.

# In[31]:


# A function to display this nicely in the Jupyter output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))


# ## Running the Summarization
# Finally, we run the summarization on a few example URLs.

# In[41]:


display_summary("https://opportunitiesforyoungkenyans.co.ke/")


# In[33]:


display_summary("https://cnn.com")


# In[34]:


display_summary("https://anthropic.com")


# In[36]:


display_summary("https://www.dstv.com/en-ke/")


# In[40]:


display_summary("https://www.kcau.ac.ke/")


# ## Conclusion
# This notebook provides a basic framework for summarizing web pages using the DeepSeek API. The code is structured to be easily extendable, and the commented-out OpenAI API code provides an alternative approach for those who might want to compare or switch between different APIs.
# 
# Feel free to fork this repository and adapt it to your needs!

# In[ ]:




