str1=input()
str2=""
for i in str1:
    if i not in str2:
        str2=str2+i
print(str2)