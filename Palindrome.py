phr = input('Enter your phrase: ')

counter = len(phr) - 1
pal_check = True

for i in range(len(phr) - 1):
    if phr[i] == phr[counter]:
        pal_check = True
        counter -= 1
    else:
        pal_check = False
if pal_check == True:
    print('your Phrase is Palindrome')
else:
    print('your Phrase is not Palindrome')