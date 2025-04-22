lst=list(map(int,input().split()))
lst1=[]
l=len(lst)
print(l)
for i in range((l-1),-1,-1):
    print(i)
    lst1.append(lst[i])
print(lst)
print(lst1)