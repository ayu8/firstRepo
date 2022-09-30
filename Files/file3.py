#count and display the number of vowels, consonants, upper and lower characters in string
string = input('Enter String')

vowels=0
consonants=0
upper=0
lower=0
for ch in string:
  if ch.isalpha():
     if ch in 'aeiouAEIOU':
         vowels +=1
     else :
         consonants +=1

     if ch.isupper():
         upper+=1
     elif ch.islower():
         lower+=1
        
print('No. of vowels =',vowels)
print('No. of consonants =',consonants)
print('No. of upper =',upper)
print('No. of lower =',lower)
