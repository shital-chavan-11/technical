list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=[]
for i in list1:
    if i in list2:
        if i not in list3:
            list3.append(i)
print(list3)