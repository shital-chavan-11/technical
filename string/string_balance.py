str1=input()
count=0
for i in str1:
    if i=="{":
        if "}" in str1:
            count=count+2
    if i=="]":
        if "[" in str1:
            count=count+2
    if i==")":
        if "(" in str1:
            count=count+2
str2="{}[]()"
k=0
for i in str1:
    if i in str2:
        k=k+1
if k==count:
    print("string is balanced")
else:
    print("string not balanced")

        
