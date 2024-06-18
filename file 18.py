ana1,ana2=input("enter first string: ").split()
count=0
if(len(ana1)==len(ana2)):
  for i in ana1:
   for j in ana2:
      if(i==j):
        count+=1
      else:
        continue 
if(len(ana1)==count): print("anagram")       
else:
  print("not an anagram")