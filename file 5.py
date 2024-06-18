str=input("enter a string: ")
f = open('myfile.txt','w')
f.write(str)
f.close()