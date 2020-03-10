import requests
from bs4 import BeautifulSoup as bs


url = "https://www.linnsheriff.org/jail/current-inmates/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
response = requests.get(url, headers=headers)

soup = bs(response.content,"html.parser")
soup_html = soup.prettify
soup_tags = soup.find_all("td")


#here I am taking the soup_tags var and writing to a txt file on my desktop.
f = open("D:/jail text files/fileresults.txt","w+")
#for i in range(len(soup_tags)):
f.write(str(soup_tags))
f.close()


#print(soup_tags)
#print(response.content)
