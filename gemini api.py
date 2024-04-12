#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install -q -U google-generativeai')
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
result =model.generate_content(a)
to_markdown(result.text)


# In[ ]:


import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


# In[ ]:


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# In[ ]:


genai.configure(api_key="GOOGLE-API-HERE")


# In[ ]:


model = genai.GenerativeModel('gemini-pro')


# In[ ]:


a = input()
result =model.generate_content(a)
to_markdown(result.text)


# In[ ]:




