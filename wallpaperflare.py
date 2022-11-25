import os
import requests
from bs4 import BeautifulSoup

query = "cod"


def log(message):
	print("[+] "+message+" ...")


URL = f"https://www.wallpaperflare.com/search?wallpaper={query}"

r = requests.get(URL,headers = {'User-agent':'yourbot'})
soup = BeautifulSoup(r.content,'html.parser')

log("Finding all images")

img_info = soup.find_all('a',attrs={'itemprop':"url"})

imgPages = []
# Add image links to 'images' list
for img in img_info:
	imgDownloadPage = img["href"] + "/download"
	imgPages.append(imgDownloadPage)

imgLinks = []
imgCount = 1
# Get img downlaod link
for img in imgPages:
	r = requests.get(img)
	soup = BeautifulSoup(r.content,'html.parser')
	
	os.system('clear')
	log(f"Getting Image Download Links {imgCount}/{len(imgPages)}")
	imgCount += 1

	# Append the download in 'imgLinks' list
	img_info = soup.find('img',id='show_img')
	imgLinks.append(img_info["src"])

log("Downloading Images")

for i in imgLinks:
	os.system('wget '+ i)

log("Done")	

