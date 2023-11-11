"""Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""
import logging
import sys

#Шестнадцатеричные цифры
h_nums = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
          8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
logging.basicConfig(level=logging.INFO, encoding='utf-8', filename="hex_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
#n = int(input('Введите целое десятичное число: '))
n = sys.argv[1]
logging.info(f'Получен параметр {n}')
try:
    n = int(n)
    logging.info(f'Дано десятичное число {n}')
    hex_n = hex(n)   #Вычисляем 16тиричное представление n при помощи hex()
    logging.info(f'Получено 16тиричное представление {n} при помощи hex(): {hex_n}')
    #Вычисляем 16тиричное представление n "вручную"
    calculate_n = ''
    while n>0:
        logging.info(f'Вычисляем 16тиричную цифру {h_nums[n%16]} и добавляем её к числу: 0x{calculate_n}')
        calculate_n = h_nums[n%16] + calculate_n
        logging.info(f'Делим нацело {n} на 16: {n//16}')
        n //= 16
    logging.info(f'16тиричное представление {sys.argv[1]} вычислено "вручную": 0x{calculate_n}')
    print(f'Без использования hex: 0x{calculate_n}')
    print(f'С использованием hex:  {hex_n}')
    if '0x'+str(calculate_n) == str(hex_n):
        logging.info(f'16тиричные представления, вычисленные "вручную" и с помощью hex(), совпадают')
except ValueError:
    logging.warning(f'Ошибка ввода! {n} не является целым десятичным числом')
    print('Ошибка ввода!')
