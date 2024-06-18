import string
str3="Hello world, Darsha this side...!!"
str3=str3.translate(str.maketrans('', '', string.punctuation))
print(str3)