import soup
import link_extract
import write_file

url=raw_input("give a url you want to scrape:\n> ")

unvisited=[url]
visited=["\n"]

file=write_file.Write_operations(url,visited,"visited_list.txt")

file.create_file()

stopping_condition=raw_input("after how many pages should the code stop fetching pages?\n> ")

while len(unvisited)>0 and len(visited)<=int(stopping_condition):
	data=soup.Organise(unvisited[0])
	(soup, url_add)=data.soup_data()
	visited.append(url_add)
	file.write_links()	
	
	print"",len(unvisited)
	
	link_list=link_extract.Extract(soup,visited,url)
	unvisited.append(link_list.extract_link())	

print"", visited
print"",unvisited