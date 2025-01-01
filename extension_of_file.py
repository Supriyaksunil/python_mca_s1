name=input("Enter file name:")
if '.' in name:
    e=name.split('.')
    print(e[-1])
else:
    print("The file has no extension")