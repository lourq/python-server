x = 10

def get_x() :
    return x

def hello() -> str :
    return 'Hello'

def print_x() -> None:
    print( "x =" , get_x() )

def change_x(value : int = 20) -> None :
    '''Comment'''
    x = value
    print('Changed to' , x)

def set_x(value : int = 20) -> None :
    global x 
    x = value
    print('Changed to' , x)

def pair():
    return 1 , 2

def main() :
    change_x(1.5)
    print( 'x = ' , get_x())
    set_x(30)
    print( 'x = ' , get_x())

    y , w = pair()
    print(f'y={y} , w={w}')

    print('y=%d , w=%d' % pair())


if __name__ == '__main__' : main()

# region hw 1

# Реалізувати програму для введення двох різних позитивних
# чисел та розрахунок їх суми. Якщо числа негативні або однакові
# пропонується повторне введення
# > Введіть х = -1
# Число має бути додатнім
# > Введіть х = 1
# > Введіть y = -1
# Число має бути додатнім
# > Введіть y = 1
# Числа мають відрізнятись
# > Введіть y = 2
# 1 + 2 = 3
    
# def custom_input(num: str) -> int:
#     return int(input(f'Input number {num} -> '))

# def check_num(a: int = 0, b: int = 0) -> bool:
#     return a != b and a >= 0 and b >= 0

# while True: 
#     x = custom_input('x')
#     y = custom_input('y')
#     if check_num(x, y):
#         print(x + y)
#         break

# endregion