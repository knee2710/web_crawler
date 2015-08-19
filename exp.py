import soup
import link_extract
import write_file

url=raw_input("give a url you want to scrape\n> ")
visited=[]
unvisited=[url]

file=write_file.Write_operations(url,visited,"visited_list.txt")
file.create_file()

data=soup.Organise(url)
(soup, url_add)=data.soup_data()
visited.append(url_add)
file.write_links()	

link_list=link_extract.Extract(soup,visited,url)
unvisited.append(link_list.extract_link())

#print"",visited
print"",unvisited
