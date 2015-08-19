from bs4 import BeautifulSoup
import requests

class Organise(object):
	
	def __init__(self, url):
		self.url=url
	
	def soup_data(self):
		source_code=requests.get(self.url)
		data=source_code.text
		soup=BeautifulSoup(data,"html.parser")
		return soup, self.url
		
	
