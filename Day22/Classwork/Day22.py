name = input('შეიყვანე შენი სახელი')
age = int(input('შეიყვანე შენი ასაკი'))
expreience = int(input('შეიყვანე შენი გამოცდილება'))

if age > 22 and expreience > 2:
    print('hired')
elif age > 25 and expreience > 1:
        print('hired')
elif age > 20 and expreience > 3:
        print('hired')
elif name == 'გურამი':
      print('hired')
else:
      print('Not hired')