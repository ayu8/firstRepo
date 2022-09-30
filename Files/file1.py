#program to check if the year enterted by the user is a leap year
a = int(input(''))
for i in range (a) :
    x = int(input('Enter Year: '))
    if x%400==0:
        print(x,'is a Leap Year')
    elif x%100==0:
        print(x,'is not a Leap Year')
    elif x%4==0:
        print(x,'is a Leap Year')
    else :
        print(x,"isn't a Leap Year")
        
