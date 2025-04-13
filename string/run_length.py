N=int(input(""))
result=[]
list3=[]
for i in range(1,N+1):
    name=input(" ")
    score=input("")
    list3.append(score)
    list1=[score,name]
    result.append(list1)
result1=sorted(result)
 