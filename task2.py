'''Вы работаете над разработкой программы для проверки корректности даты,
введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата
корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или
"False" (дата не корректна) в зависимости от результата проверки'''

import logging
import sys

logging.basicConfig(level=logging.INFO, encoding='utf-8', filename="date_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

date = sys.argv[1]
logging.info(f'Получена дата в формате день.месяц.год: {date}')

if len(date.split('.'))!=3:
    logging.warning('Неверный формат даты!')
    result = False
else:
    try:
        d,m,y = [int(x) for x in date.split('.')]
        if 1<=y<=9999:
            if m==2:
                if (y%4==0 and y%100!=0) or (y%400==0):
                    result = 0<d<=29
                    if result: logging.info(f'Дата корректна: {d}.02.{y} (високосный год)')
                    else: logging.warning(f'Дата не корректна! В феврале 29 дней ({y} - високосный год) ')
                else:
                    result = 0<d<=28
                    if result: logging.info(f'Дата корректна: {d}.02.{y} (не високосный год)')
                    else: logging.warning(f'Дата не корректна! В феврале 28 дней ({y} - не високосный год)')
            elif m in (1,3,5,7,8,10,12):
                result = 0<d<=31
                if result: logging.info(f'Дата корректна: {d}.{m}.{y}')
                else: logging.warning(f'Дата не корректна! В {m} месяце 31 день')
            elif m in (4,6,9,11):
                result = 0<d<=30
                if result: logging.info(f'Дата корректна: {d}.{m}.{y}')
                else: logging.warning(f'Дата не корректна! В {m} месяце 30 дней') 
            else:
                result = False
                logging.warning(f'Дата не корректна! Неверно указан месяц: {m}!')
        else:
            result = False
            logging.warning(f'Неверно указан год: {y}!')
    except ValueError:
        logging.warning('Неверный формат даты!')
        result = False


print(result)