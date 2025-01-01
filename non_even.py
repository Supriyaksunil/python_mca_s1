
numbers=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    num=int(input("Enter element"))
    numbers.append(num)
print(numbers)
odd=[]
for i in numbers:
    if i%2!=0:
        odd.append(i)

print(odd)