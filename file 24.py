x,y,z=input("enter numbers and (a-add,s-subtract,m-multiply,d-division): ").split()
x,y=int(x),int(y)
match (z):
 case 'a':
   print(x+y)
 case 's':
   print(x-y)
 case 'm':
   print(x*y)
 case 'd':
   print(x / y)