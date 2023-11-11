'''Треугольник существует только тогда, когда сумма любых двух
его сторон больше третьей. Дано a, b, c - стороны предполагаемого
треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется
больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.'''

import logging
import sys

def sides_of_triangle():
    sides = sys.argv[1:]
    logging.info(f'Получены параметры: {sides}')
    if len(sides) < 3:
        print('Недостаточно параметров')
        logging.info(f'Недостаточно параметров:')
        return False    
    for i in range(len(sides)):
        try:
            sides[i] = int(sides[i])
            if sides[i]<=0:
                logging.warning(f'Ошибка ввода! {sides[i]} - отрицательное число')
                return False
        except ValueError:
            print(f'Неверный ввод. {sides[i]} - не является целым числом')
            logging.warning(f'Ошибка ввода! {sides[i]} - не является целым числом')
            return False
    return sides
def is_triangle(sides):
    a,b,c = sides
    logging.info(f'{a}+{b}>{c} - {a + b > c}')
    logging.info(f'{a}+{c}>{b} - {a + c > b}')
    logging.info(f'{b}+{c}>{a} - {b + c > a}')
    if a + b > c and a + c > b and b + c > a:
        logging.info(f'Треугольник со сторонами {a}, {b}, {c} существует')
        print(f'Треугольник существует')
        return True
    else:
        logging.info(f'Треугольник со сторонами {a}, {b}, {c} не существует')
        print(f'Треугольник не существует')
        return False

def type_of_triangle(sides):
    a,b,c = sides
    logging.info(f'{a}={b} - {a == b}')
    logging.info(f'{a}={c} - {a == c}')
    logging.info(f'{b}={c} - {b == c}')
    if a == b == c:
        logging.info(f'Треугольник со сторонами {a}, {b}, {c} является равносторонним')
        return f'Треугольник со сторонами {a}, {b}, {c} является равносторонним'
    elif a == b or a == c or b == c:
        logging.info(f'Треугольник со сторонами {a}, {b}, {c} является равнобедренным')
        return f'Треугольник со сторонами {a}, {b}, {c} является равнобедренным'
    else:
        logging.info(f'Треугольник со сторонами {a}, {b}, {c} является разносторонним')
        return f'Треугольник со сторонами {a}, {b}, {c} является разносторонним'


logging.basicConfig(level=logging.INFO, encoding='utf-8', filename="triangle_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
sides = sides_of_triangle()
if sides and is_triangle(sides):
    print(type_of_triangle(sides))