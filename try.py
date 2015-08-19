s=[]
s.append("neeraj")
s.append("manvitha")
file=open("p.txt",'a')


file.writelines(["\n"]+s[:])

file=open("p.txt")
print"",file.read()
