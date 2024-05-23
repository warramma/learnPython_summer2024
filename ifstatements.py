#you wake up
print('You have awakened.')

choice = ''
weather = ''
day = ''
dinner = ''
#are you hungry? if so, eat breakfast
choice = input('Are you hungry? (Y/N): ')
if(choice.lower() == 'y'):
    print('Eat some breakfast before you head out!')
else:
    print('Make sure to pack a heavier lunch today!')

#do you have class today? if so go to class, else stay home
choice = input('Do you have class today? (Y/N): ')
if(choice.lower()=='y'):
    #if you leave the house, check if its rainy, sunny, hot
    print('You better get a move on slowpoke.')
    weather = input('Is it cloudy or sunny today? ')
    if(weather.lower() == 'cloudy'):
        print('Make sure to bring an umbrella just in case!')
    if(weather.lower()== 'sunny'):
        print('Make sure to bring your sunglasses!')
    
    #if it's MWF, go to math class. If its TTH, go to CS class
    day = input('What is the day of the week? Monday, Tuesday, Wednesday, Thursday, or Friday?: ')
    if(day.lower()=='monday' or day.lower()=='wednesday' or day.lower()=='friday'):
        print('You have math today, make sure to bring your math materials!')
    else:
        print('You have your CS classes today, don\'t forget your laptop!')
else:
    print('Nice! Enjoy your day off :)')

print('.....')
print('.....')
print('.....')
print('...You\'re back from school...')
print('What would you like for dinner?')
print('1. Pasta')
print('2. Nasi dan ayam')
print('3. make your own sandwich')
print('4. all the above')
dinner = input('Enter a number from 1 thru 4 to choose: ')

if(int(dinner) == 1):
    print('Pasta it is')
elif(int(dinner)==2):
    print('nice, rice and chicken')
elif(int(dinner)==3):
    print('yum a sandwich!')
else:
    print('alright! time to eattt')