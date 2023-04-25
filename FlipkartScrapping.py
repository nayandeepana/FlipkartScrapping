import requests
import pandas as pd
from bs4 import BeautifulSoup
Product_price=[]
Product_name=[]
Product_Discription=[]
for i in range(1,20):

    url=f"https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+10000%7CMobiles&requestId=ff949b27-11ef-4d15-9e33-553f870bf06f&as-backfill=on&page={i}"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    # print(soup)

    pname=soup.findAll("div",class_="_4rR01T")
    for i in pname:
        Product_name.append(i.text)



    price=soup.findAll("div",class_="_30jeq3 _1_WHN1")
    for i in price:
        Product_price.append(i.text)

    pdisc=soup.findAll("ul",class_="_1xgFaf")
    for i in pdisc:
        Product_Discription.append(i.text)

df=pd.DataFrame({"Name":Product_name,"Discription":Product_Discription,"Price":Product_price})
print(df)
df.to_csv("Flipkart.csv")

'''
NOTE: Change url for your Choices of search
'''