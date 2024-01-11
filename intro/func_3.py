x = 10

def get_x() :
    return x

def hello() -> str :
    return 'Hello'

def print_x() :
    print( "x = " , get_x() )

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
    
def custom_input(num: str) -> int:
    return int(input(f'Input number {num} -> '))

def check_num(a: int, b: int) -> bool:
    return a != b and a >= 0 and b >= 0

while True: 
    x = custom_input('x')
    y = custom_input('y')
    if check_num(x, y):
        print(x + y)
        break