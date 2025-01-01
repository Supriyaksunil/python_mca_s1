start=int(input("Enter start year:"))
end=int(input("Enter end year:"))
print("The leap year between",start,"and",end,"are: ")
for i in range(start,end):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)