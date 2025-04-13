import string
list1=list(string.ascii_lowercase)
list2=list(string.ascii_uppercase)
str1=input()
count=0
for i in str1:
    if i in list1 or list1:
        count=count+1
if count==len(str1):
    print("panagram")
else:
    print("not panagram")