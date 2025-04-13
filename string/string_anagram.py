str1=input()
str2=input()
count=0
for i in str1:
    if i in str2:count=count+1
if count==len(str2):
    print("anagram")
else:
    print("not anagram")