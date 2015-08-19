from bs4 import BeautifulSoup
import urlparse

class Extract(object):

	unvisited=[]
	def __init__(self,soup, visited, url):
		self.soup=soup
		self.visited=visited
		self.url=url
	
	def extract_link(self):
		for link in self.soup.find_all("a"):
			new_tag=urlparse.urljoin(self.url,link.get("href"))		
			if self.url in new_tag and new_tag not in self.visited:
				self.unvisited.append(new_tag)
		return self.unvisited		