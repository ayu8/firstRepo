#program for grades distribution
a=int(input())
for i in range (a):
    x = float(input('Enter Your Percentage : '))
    if x>100 :
        print('Please Enter Correct Percentage i.e. not more than 100%')
    elif x>90 and x<101 :
        print('Your Grade is A')
    elif x>80 and x<91:
        print('Your Grade is B')
    elif x>70 and x<81 :
        print('Your Grade is c')
    elif x>60 and x<71 :
        print('Your Grade is D')
    elif x<0 :
        print('Please Enter Correct Percentage i.e. not less than 0%')
    else :
        print('Your Grade is E')
