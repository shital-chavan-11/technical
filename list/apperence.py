lst=list(map(int,input().split()))
list1=[]
list2=[]
for i in lst:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
list1.extend(list2)
print(list1)