import random
f = True
while f:
    try:
        s = input("enter names separated by space: ")
        s = s.split()
        i = random.randint(0, len(s)-1)
        print(f'{s[i]} is smoking')
        f = False
    except ValueError:
        print(f'try again')
