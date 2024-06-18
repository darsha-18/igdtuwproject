str=input("enter a string: ")
f = open('myfile.txt','r')   
text=f.read()
print(len(text))