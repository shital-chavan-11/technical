str1=input()
str3=""
for i in str1:
    str3=i+str3
if str3==str1:
    print("palindrome")
else:
    print("not palindrome")