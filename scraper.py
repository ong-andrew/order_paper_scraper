import requests
from bs4 import BeautifulSoup

url = "https://www.parlimen.gov.my/takwim-dewan-rakyat.html?uweb=dr#"
headers = {'user-agent': 'my-agent/1.0.1'}

soup = BeautifulSoup(requests.get(url, headers=headers).text)
table = soup.find("table") #find table tag

links = table.find_all(['td','a'])

def scraper():
    output = ""
    for link in links:
        output += link.text + "\n"
        if(link.get('href') == None):
            pass
        else:
            output += link.get('href') + "\n"

    with open('temp.txt', 'w') as data: #create a temp file to store latest scrape
        data.writelines(output)
