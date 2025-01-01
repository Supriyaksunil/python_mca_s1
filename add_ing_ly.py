string=input("Enter string:")
if string[-3:]=="ing":
    string+='ly'
else:
    string+='ing'
print(string)