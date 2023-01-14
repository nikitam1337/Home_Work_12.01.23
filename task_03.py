# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

print()
metod = input(
    'Выберите реализацию RLE алгоритма:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')

while not metod.isdigit():
    print(f'{metod} - не цифра! Попробуйте снова.')
    metod = input(
        'Введите цифру:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')

while int(metod) < 1 or int(metod) > 2:
    print(f'Введите цифру 1 или 2:', end=" ")
    metod = input()
    while not metod.isdigit():
        print(f'{metod} - не цифра! Попробуйте снова.')
        metod = input(
            'Введите цифру:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')

if int(metod) == 1:
    input_data = input(
        'Вы выбрали модуль сжатия данных. Введите текст для сжатия:\n')
    output_data = ''
    i = 0
    while i < len(input_data):
        count = 1
        while i + 1 < len(input_data) and input_data[i] == input_data[i + 1]:
            count = count + 1
            i = i + 1
        output_data += str(count) + input_data[i]
        i = i + 1
    print(f'Сжатые данные: {output_data}')

else:
    input_data = input(
        'Вы выбрали модуль восстановления данных. Введите текст для восстановления:\n')
    output_data = ''
    if len(input_data) == 1:
        print(f'Ошибка ввода! Должно быть минимум 2 символа!')

    elif input_data.isdigit():
        if len(input_data) % 2 != 0:
            print(f'Ошибка ввода! Должно быть четное число символов!')
        else:
            i = 0
            while i < len(input_data)-1:
                output_data += input_data[i+1]*int(input_data[i])
                i = i + 2
            print(f'Данные до сжатия: {output_data}')

    elif input_data[-1].isdigit():
        print('Некорректный ввод данных, последний элемент должен быть буквой. Либо весь текст должен состоять только из цифр.')
    else:
        temp_string = ''
        flag = 0
        for i in range(1, len(input_data)):    
            if (not input_data[0].isdigit()) or (not input_data[i-1].isdigit() and not input_data[i].isdigit()): # Проверка, на задвоение букв или отстутсвие цифры в самом начале
                print(f'Ошибка ввода! Перед {i}-м символом нет цифры!')
                flag = 1
                break
            elif input_data[i-1].isdigit():
                temp_string += input_data[i-1]    
            else:
                temp_string += f' {input_data[i-1]} '
        if input_data[-1].isdigit():
            temp_string += input_data[-1]   
        else:
            temp_string += f' {input_data[-1]} '

        if flag == 0:
            temp_list = temp_string.split()
            i = 0
            while i < len(temp_list)-1:
                output_data += temp_list[i+1]*int(temp_list[i])
                i = i + 2
            print(f'Данные до сжатия: {output_data}')
