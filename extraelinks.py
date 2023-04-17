import requests
import re
from bs4 import BeautifulSoup
url = "https://www.xvideos.com/c/Gay_interracial-123"
input(
    f"introduce una url, por ejemplo {url}")
print(f"Has introducido {url}")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Encuentra todos los elementos <a> que contienen "video" en el atributo href
video_links = [link["href"] for link in soup.find_all(
    "a") if "video" in link.get("href")]
with open("template.txt", "w", encoding="utf-8") as file:
    for link in video_links:
        file.write(str(link) + "\n")

patron = re.compile(r'(\/)(video\d+\/.*)')
patron_url = re.compile(r'(https:\/\/www\.)(.*)(\.com)')
url_base = re.match(patron_url, url)
if url_base:
    base = url_base.group(0)

with open('template.txt', 'r') as f_input:
    lineas = f_input.readlines()
with open('video_links.txt', 'w', encoding="utf-8") as f_output:
    repit = 0
    for linea in lineas:
        coincidencias = re.match(patron, str(linea))
        repit = repit + 1
        if repit == 0:
            if coincidencias:
                f_output.write(base + coincidencias.group(0) + "\n")
        else:
            repit = - 1
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
