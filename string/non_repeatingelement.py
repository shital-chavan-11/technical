str1=input()
str2=""
for i in str1:
    k=str1.count(i)
    if k==1:
         str2=str2+i
    else:
        print("there is not non repeating character in this string")
print("the first non repeating character is",str2[0])