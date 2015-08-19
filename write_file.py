class Write_operations(object):
	
	def __init__(self,url,visited,file_name):
		self.url=url
		self.visited=visited
		self.file_name=file_name
		
		
	def create_file(self):
		with open(self.file_name,'a') as file:
			file.write("\nfor "+self.url+" :\n"+"\n" +self.file_name+":\n")
		
		
	def write_links(self):
		file=open(self.file_name,'a')
		file.writelines(self.visited[:]+["\n"])