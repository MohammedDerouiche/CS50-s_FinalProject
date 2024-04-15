import requests
from bs4 import BeautifulSoup

jobTitle = "Data Anlsyt"
jobTitle = jobTitle.replace(" ", "+")
url = f"https://www.google.com/search?q={jobTitle}+skills"

print(url)
responce = requests.get(url=url)
print(responce.text)
# print(responce)
# soup = BeautifulSoup(responce.text, "html.parser")
# data = soup.find_all('div', attrs={'jsname': 'ibnC6b'})
# print(data)