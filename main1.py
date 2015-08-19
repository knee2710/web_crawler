import urlparse
from bs4 import BeautifulSoup
import requests

url="http://www.9gag.com"

unvisited=[url]
visited=[]

stopping_condition=raw_input("after how many pages should the code stop fetching pages?\n> ")

while len(unvisited)>0 and len(visited)<=int(stopping_condition):
	try:
		htmltext1=requests.get(unvisited[0])
		htmltext=htmltext1.text
	except:
		print urls[0]
	soup=BeautifulSoup(htmltext,"html.parser")
	
	visited.append(unvisited.pop(0))
	print"",len(unvisited)
	
	for tag in soup.find_all('a'):
		new_tag=urlparse.urljoin(url,tag.get("href"))
		if url in new_tag and new_tag not in visited:
			unvisited.append(new_tag)
			

print"",visited
	
	
