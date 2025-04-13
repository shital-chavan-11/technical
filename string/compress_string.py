str1=input()
str2=""
for i in str1:
    a=str(str1.count(i))
    if i not in str2:
        str2=str2+i+a
print(str2)