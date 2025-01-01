l1=[]
l2=[]
n=int(input("Enter limit"))
for i in range(n):
    u=int(input("Enter value:"))
    l1.append(u)
print(l1)
m=int(input("Enter limit:"))
for i in range(m):
    v=int(input("Enter value:"))
    l2.append(v)
print(l2)
if len(l1)==len(l2):
    print("length are same")
else:
    print("length are not same")
if sum(l1)==sum(l2):
    print("sum is same")
else:
    print("sum is not same")
flag=0
for x in l2:
    if x in l1:
        flag=1
if flag==1:
    print("There is  common element")
else:
    print("There is no common element")


