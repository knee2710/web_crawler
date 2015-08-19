import urlparse
import requests
from bs4 import BeautifulSoup

url=raw_input("give a url you want to scrape:\n> ")

unvisited=[url]
visited=["\n"]

file1 = open("lists_vis.txt",'a')
file2 = open("lists_unvis.txt",'a')
file1.write("\nfor "+url+" :\n"+"\nvisited links:\n")
file2.write("\nfor "+url+" :\n"+"\nunvisited links:\n")

stopping_condition=raw_input("after how many pages should the code stop fetching pages?\n> ")

while len(unvisited)>0 and len(visited)<=int(stopping_condition):
	source_code=requests.get(unvisited[0])
	data=source_code.text
	soup=BeautifulSoup(data,"html.parser")
	visited.append(unvisited.pop(0))
	file1.writelines(visited[:]+["\n"])
	print"",len(unvisited)

	for link in soup.find_all("a"):
		new_tag=urlparse.urljoin(url,link.get("href"))		#join the urls to make it a proper url (with http://...) in case it wasn't
		if url in new_tag and new_tag not in visited:
			unvisited.append(new_tag)			
		
file2.writelines(unvisited) 

print"", visited