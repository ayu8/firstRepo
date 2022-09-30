#input a string & determine whether it is palindrom or not ,
#convert the case of characters in a string.
# e.g. radar
string = input('Enter String')
newstr=''
for ch in string:
    if ch.islower():
        newstr=newstr+ch.upper()
    elif ch.isupper():
        newstr=newstr+ch.lower()

print('Old string =',string)
print('New String =',newstr)

