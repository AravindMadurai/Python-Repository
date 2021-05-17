'''
Web Scrapping for POCO M3 product
'''
import requests  #Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import matplotlib.pyplot as plt
import numpy as npy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
M3_reviews=[]

### Extracting reviews from Amazon website ################
for i in range(1,10):
  ip=[]  
  url="https://www.amazon.in/POCO-M3-Power-Black-Storage/product-reviews/B08WJB96PC/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  M3_reviews=M3_reviews+ip  # adding the reviews of one page to empty list which in future contains all the reviews

# writing reviews in a text file 
with open("POCO_M3.txt","w",encoding='utf8') as output:
    output.write(str(M3_reviews))
#Word Cloud
dataset = open("POCO_M3.txt","r",encoding='utf8').read()
wordcloud = WordCloud(background_color="white",max_words=len(dataset),max_font_size=40, relative_scaling=.5).generate(dataset)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#sentimental analysis
