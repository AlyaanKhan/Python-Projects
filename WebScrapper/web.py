import requests
from bs4 import BeautifulSoup
def web_scrapper():
    url = "https://www.techtarget.com/searchenterpriseai/definition/convolutional-neural-network"
    response = requests.get(url)
    print(response)
    html_parsing = BeautifulSoup(response.content, 'html.parser')D
    finding = html_parsing.find_all('h2', class_='section-title')
    with open ('titles_scrapped.txt', 'w') as file:
        for findings in finding:
            file.write(findings.get_text() + '\n')
    print(f"Data '{findings}' written successfully in file")
web_scrapper()
