import streamlit as st
import requests
import time
from newsapi import NewsApiClient
import os

api=os.getenv('newsapi')
news=NewsApiClient(api_key=api)
st.title("Get latest news here.....")
col1,col2= st.columns(2)
with col1:
    city=st.selectbox("Select city",['','Kolkata','Delhi','Mumbai','kerala'])
with col2:
       news_type=st.selectbox("Choose news type",['','Murder','Theft','Riots','Suicide'])
if city!='' and news_type!='':
       with st.spinner("Generating....."):
              time.sleep(3)
              statement=f"{news_type} {city}"
              data=news.get_everything(
              q=statement,
              language='en',
              sort_by='relevancy',
              page=2,
              page_size=10
              )
              articles=data['articles']
              total=data['totalResults']
              if total>1:
                     for i in range(total):
                            with st.container(height=800):
                                          tittle=articles[i]['title']
                                          des=articles[i]['description']
                                          img=articles[i]['urlToImage']
                                          
                                          st.image(img,)
                                          st.header(tittle)
                                          st.markdown(des)
                                          url=articles[i]['url']
                                          st.markdown(f"{url}")
else:
    st.markdown("Please choose the fields")
