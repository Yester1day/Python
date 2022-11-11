import random
number=input("Введите загаданное вами число в диапазоне [0;100],чтобы не забыть его: ")
x=0
y=100
tries=1
computer_number=random.randrange(x,y+1)
while x!=y:
    print("Ваше число равно,больше или меньше:",computer_number)
    z=input()
    if 'больше' in z.lower():
            x=computer_number
            computer_number=random.randrange(x,y)
            tries+=1
    elif 'меньше' in z.lower():
            y=computer_number
            computer_number=random.randrange(x,y)
            tries+=1
    elif 'равно' in z.lower():
            break
print('Ваше число:',number ,',а количество попыток:',tries)
