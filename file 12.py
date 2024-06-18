def sum_of_digits(n):
   sum=0
   rem=0
   if(n==0 or n<0):
      return 0
   while(n!=0):
      rem=n%10
      sum=sum+rem
      n=int(n/10)
   return sum   
sum=sum_of_digits(432)
print(f'sum of the digits:{sum}')