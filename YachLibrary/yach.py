import requests
from bs4 import BeautifulSoup
import os

os.remove(r"C:\Users\yigit\OneDrive\Desktop\YachLibrary\CodeHtmlYach.txt")
website = input("Web Sites Link= ")
requestweb = requests.get(website)

if requestweb.status_code == 200:
    result = BeautifulSoup(requestweb.content, 'html.parser')
    file = open("CodeHtmlYach.txt", mode="w")
    lastresult = result.prettify()
    file.write(lastresult)
else:
    print(f"Hata: {requestweb.status_code}")
