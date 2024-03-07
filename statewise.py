n=int(input("Enter no.of participants:"))
if n<=0:
    print("Invalid input")
l=[]
for i in range(n):
    name=input("Name:")
    state=input("State:")
    age=int(input("Age:"))
    if age<=10 or age>80:
        print("Invalid input")
    l.append({'Name':name,'State':state,'Age':age})
print("Here's the list of participants details:")
for i in l:
    print(i)
res={}
for i in l:
    if i['State'] in res.keys():
        res[i['State']] +=1
    else:
        res[i['State']]=1
for x,y in res.items():
    print("State:",x,"Count:",y)