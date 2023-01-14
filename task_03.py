# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Пояснения к решению: Удалось реализовать модули сжатия как для цифр, так и для букв. 
# Но вот с модулем восстановления из цифр я не могу понять. Как определить при ручном вводе, какое число отображает кол-во повторений,
# а какое уже саму повторяющуюся цифру. К примеру:  3415117 - это либо 3 раза повторяется 4, либо же 34 раза единица. и т.д.

print()
metod = input('Выберите реализацию RLE алгоритма:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')

while not metod.isdigit():
        print(f'{metod} - не цифра! Попробуйте снова.')
        metod = input('Введите цифру:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')
while int(metod) < 1 or int(metod) > 2:
    print(f'Введите цифру 1 или 2:', end = " ")
    metod = input()
    while not metod.isdigit():
        print(f'{metod} - не цифра! Попробуйте снова.')
        metod = input('Введите цифру:\n1 - модуль сжатия данных;\n2 - модуль восстановления данных.\n: ')

print(metod)

if int(metod) ==1: 
    input_data = input('Вы выбрали модуль сжатия данных. Введите текст для сжатия:\n')
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
    input_data = input('Вы выбрали модуль восстановления данных. Введите текст для восстановления:\n')
    temp_string =''

    for i in range(len(input_data)):
        if input_data[i].isdigit():
            temp_string += input_data[i]
        else:
            temp_string += f' {input_data[i]} '
    temp_list = temp_string.split()

    if temp_list[-1].isdigit():
        print('Некорректный ввод данных, последний элемент должен быть буквой ')
    else:
        output_data = ''
        i=0
        while i < len(temp_list):
            output_data += temp_list[i+1]*int(temp_list[i])
            i = i + 2   
        print(f'Данные до сжатия: {output_data}')
