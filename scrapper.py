from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("./chromedriver")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers=["name","lightyearsfromearth","planetmass","stellarmagnitude","discoverydate"]
    planetdata=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class","exoplanet"}):
            litags=ultag.find_all("li")
            templist=[]
            for  index,litag in enumerate(litags):
                if index==0:
                    templist.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append("")
            planetdata.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrape()