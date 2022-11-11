#отгадай число
#it gonna be interested
#случайное число в диапозоне от 1 до 100
import random
print('\tДобро пожаловать в мою игру по отгадыванию чисел')
print('Я загадал натуральное число от 1 до 100.')
print('Попытайся отгадать его за минимальное число попыток!\n')
the_number=random.randint(1,100)
guess=int(input("Ваше предположение: "))
tries=1    
#начинаем отгадывать
while guess !=the_number or tries>6:
     if guess>the_number:
         print("Меньше...")
     if guess<the_number:
         print("Больше...")
     else:
          print('У вас закончились попытки')
          break
     guess=int(input("Ваше предложение: "))
     tries+=1    
print('Вам удалось отгадать число, это действительно',the_number)
print("На это Вам понадобилось всего",tries,"попыток.\n")
input('\n\nНажмите Enter, чтобы выйти!')

 
 
