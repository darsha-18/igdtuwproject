value,convert_to=input("enter the value and convert to(c-celcuius, f-fahrenheit): ").split()
value=int(value)
match (convert_to):
 case 'c':
   print((value-32)/1.8)
 case 'f':
   print((value * 1.8) + 32)