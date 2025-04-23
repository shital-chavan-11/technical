lst=list(map(int,input().split()))
list1=[]
l=len(lst)
for i in range(0,l+1):
    for j in range(i,l+1):
        s=[lst[i]]
        list1.append(s)
print(list1)