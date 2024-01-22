from random import randint


random_num = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    supposition = int(input('Введите число: '))
    if supposition < random_num:
        print('Ваше число меньше того, что загадано')
    elif supposition > random_num:
        print('Ваше число больше того, что загадано')
    else:
        break

print('Отличная интуиция! Вы угадали число :)')