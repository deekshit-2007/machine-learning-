s = input("enter a string:")
vowels = 0
consonants = 0
for i in s:
    if i == 'a'or i=='e'or i=='i'or i =='o'or i =='u'or\
       i == 'A'or i=='E' or i=='I'or i=='O'or i=='U':
        vowels = vowels+1
    elif i.isalpha():
        consonants=consonants+1
print("number of vowels",vowels)
print("number of consonants",consonants)