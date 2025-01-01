names=["ammu","appu","arun"]
count=0
for x in names:
    for i in x:
        if i=="a":
            count+=1
print("number of a in the list",names,"is",count)