import pandas as pd
import requests
from openpyxl.workbook import Workbook
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlencode,urljoin
from datetime import datetime


## Scrap HTML File
with open("home.html","r") as html_file:
    content = html_file.read()

    # Return HTML
    soup1 = BeautifulSoup(content,"html.parser")

    # Return First h5 tag
    tags1 = soup1.find("h5")
    
    # Return All h5 tag
    courses_html_tags = soup1.find_all("h5")
    for course in courses_html_tags:
        print(course.text)          # Return Text Inside Tag

    course_cards = soup1.find_all("div",class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} costs {course_price}")




## Scrap Website   
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=").text
soup2 = BeautifulSoup(html_text,"html.parser")
jobs = soup2.find_all("li",class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    published_date = job.find("span",class_="sim-posted").span.text
    if("few" in published_date):
        company_name = job.find("h3",class_="joblist-comp-name").text.strip()
        skills = job.find("span",class_="srp-skills").text.strip()
        more_info = job.header.h2.a["href"]
        print(more_info)
        print(f"Company Name : {company_name}\nRequired Skills : {skills}\nPUblished Date : {published_date}\nMore Info : {more_info}")
        print("*"*100)




## Scrap Top 250 IMDB Movie
url = "https://www.imdb.com/chart/top/"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
response = requests.get(url,headers=headers)
soup3 = BeautifulSoup(response.text,"html.parser")


# Return HTML
contents = soup3.prettify()

movie_title,movie_year,movie_rating = [],[],[]
movie = soup3.find_all("div",class_="sc-be6f1408-0 gVGktK cli-children")

for i in movie:
    movie_title.append(i.find("h3").text)
    movie_rating.append(i.find("span",class_="ipc-rating-star").text[0:3])
    movie_year.append(i.find("span",class_="sc-be6f1408-8 fcCUPU cli-title-metadata-item").text)


# Creating DataFrame
movie_df = pd.DataFrame({"Movie Title":movie_title,"Year of Release":movie_year,"IMDB Rating":movie_rating})
print(movie_df)




## BBC Weather Scrap
required_city = "MUmbai"
location_url = "https://locator-service.api.bbci.co.uk/locations?" + urlencode({
   'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
   's': required_city,
   'stack': 'aws',
   'locale': 'en',
   'filter': 'international',
   'place-types': 'settlement,airport,district',
   'order': 'importance',
   'a': 'true',
   'format': 'json'
})
result = requests.get(location_url).json()


# url to BBC weather, corresponding to a specific city (Mumbai, in this example)
url =  "https://www.bbc.com/weather/" + result["response"]["results"]["results"][0]["id"]
response = requests.get(url)


# Initiate An Instance Of BeautifulSoup
soup4 = BeautifulSoup(response.content,"html.parser")


# block-type: span; identifier type: class; and class name: wr-day-temperature__high-value 
daily_high_values = soup4.find_all("span",class_="wr-day-temperature__high-value")
daily_low_values = soup4.find_all("span",class_="wr-day-temperature__low-value")
daily_summary = soup4.find("div",class_="wr-day-summary").text


# Store High Value And Low Value In The List
daily_high_value_list = [daily_high_values[i].text.strip().split()[0] for i in range(len(daily_high_values))]
daily_low_value_list = [daily_low_values[i].text.strip().split()[0] for i in range(len(daily_high_values))]


# Split The String On UpperCase
daily_summary_list = re.findall('[a-zA-Z][^A-Z]*',daily_summary)

dateList = pd.date_range(datetime.today(),periods=len(daily_high_values)).tolist()
dateList = [dateList[i].date().strftime("%y-%m-%d") for i in  range(len(dateList))]
zipped = zip(dateList,daily_high_value_list,daily_low_value_list,daily_summary_list)


# Convert Into DataFrame
df = pd.DataFrame(list(zipped),columns=["Date","High","Low","Summary"])
print(df)


# Convert Into CSV
location = soup4.find("h1",attrs={"id":"wr-location-name-id"})
fileName_csv = location.text.split()[0] + ".csv"
df.to_csv(fileName_csv,index=None)


# Convert Into Excel
fileName_xlsx = location.text.split()[0] + ".xlsx"
df.to_excel(fileName_xlsx)