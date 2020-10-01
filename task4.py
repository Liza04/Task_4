print('Чтобы умножить числа введите "go", завершить работу - "exit"')
answer = input()
while answer.lower() == 'go':
    number_A = int(input('Введите первое число: '))
    number_B = int(input('Введите второе число: '))
    odd_B = []
    while number_A >= 1:
        if number_A % 2 != 0:
            odd_B.append(number_B)
        if number_A == 1:
            break
        number_A = number_A // 2
        number_B = number_B * 2
    print(sum(odd_B))
    answer = input()
    if answer.lower() == 'exit':
        break