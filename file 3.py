def fact(num):
   if num==1 or num==0:
     return 1
   elif num<0:
     return 0
   else:
      factnum= num * fact(num-1)
      return factnum
   
factorial=fact(number)
print(factorial)