import requests
from bs4 import  BeautifulSoup
html_text =requests.get ('https://www.glassdoor.com/Job/nigeria-data-scientist-jobs-SRCH_IL.0,7_IN177_KO8,22.htm').text

soup=BeautifulSoup(html_text,'lxml')
job=soup.find_all ('li', class_='JobsList_jobListItem__JBBUV')
company_name= soup.find_all('id', class_=)
