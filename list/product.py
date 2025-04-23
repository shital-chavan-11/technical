lst=list(map(int,input().split()))
list2=[]
k=1
for i in lst:
    k=1
    for j in lst:
        if i!=j:
            k=k*i
    list2.append(k)   
print(list2)
print(lst)