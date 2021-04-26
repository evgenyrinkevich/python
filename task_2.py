import sys


class ZeroDiv(Exception):

    @staticmethod
    def check(a, b):
        try:
            a, b = float(a), float(b)
            if b == 0:
                raise ZeroDiv
            else:
                print(f'Результат: {a / b :.2f}')
        except ValueError:
            print('Вы ввели не число')
        except ZeroDiv:
            print('Нельзя делить на 0')


if __name__ == '__main__':
    try:
        z = ZeroDiv.check(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Введите числа в терминале')
