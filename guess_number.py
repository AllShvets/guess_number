import random
num_comp = random.randint(1, 100)
user_num = int(input('Угадайте число от 1 до 100: '))

while user_num != num_comp:
    
    if user_num < num_comp:
        print('Ваше число меньше того, что загадано')
    elif user_num > num_comp:
        print('Ваше число больше того, что загадано')

    user_num = int(input('Угадайте число от 1 до 100: '))

print('Отличная интуиция! Вы угадали число :)')