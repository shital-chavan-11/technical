str1=input()
dict1={}
for i in str1:
    k=str1.count(i)
    dict1[k]=i
list1=dict1.keys()
list2=sorted(list1)
a=list2[-1]
print(dict1.get(a))