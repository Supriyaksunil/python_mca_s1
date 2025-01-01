def char_count(string):
    counts=dict()
    words=string.strip()
    for char in words:

        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1
    print(counts)
string=input("Enter the string:")
s=char_count(string)
print(s)