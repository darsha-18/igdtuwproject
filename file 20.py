x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
i=0
sum=0
for i in range(len(x)):
   sum=sum+x[i]
print(f'sum of numbers in list:{sum}') 