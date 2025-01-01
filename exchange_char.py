from pydoc import replace


def exchange_letter(str):
    if len(str)<=1:
        return str
    return str[-1]+str[1:-1]+str[0]
str=input("Enter string")
s=exchange_letter(str)
print(s)
