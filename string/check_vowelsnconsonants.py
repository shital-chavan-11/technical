str1=input()
str2="aeiouAEIOU"
k=0
p=0
for i in str1:
    if i in str2:
        k=k+1
    else:
        p=p+1
if k+p==len(str1):
    print("vowels are",k)
    print("consonants are",p)