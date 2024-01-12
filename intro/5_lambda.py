# Лямбда-вираз: вираз, який повертає функцію

lam1 = None
y = 30

def init_lam1():
    global lam1 
    y = 10
    lam1 = lambda x : print( x , y )
    # створюється у контексті init_lam1
    # при дефініції виявляється що існує посилання на "у", контекст якого локалізований 
    # - не буде доступний при виклику (з main). Відбувається capture (closure/scoped) 
    # - y capture group (лексикографічний окіл) функції додається "у" зі значенням 10

def oper(lam) -> int : 
    return lam( 1 , 2 )

# region hw 2

# Реалізувати ідею "Стратегії" - передати у функцію декілька операцій (лямбда-виразів), 
# Які будуть застосовані до однакового набору даних та визначена та з них, яка дає мінімальне значення. 
# Як приклад можна використати різні алгоритми розрахунку середнього: арифметичне, геометричне, гармонічне,....


def hw() -> None:
    x = 121
    y = 4

    arith = lambda x, y: (x + y) / 2
    geo = lambda x, y: (x * y) ** 0.5
    harm = lambda x, y: 2 * (x * y) / (x + y)
    
    print(min_val([arith, geo, harm], x, y))

def min_val(func, x, y) -> float:
    return min(f(x, y) for f in func)

# endregion

def main() -> None :
    global y
    init_lam1()
    y = 20
    lam1('Hello')
    lam2 = lambda x , y : print(x , y)
    lam2 (10 , 'qwe')
    lam3 = lambda : print('No params')
    lam3()
    # IIFE Immediately invoked functional expression - вирази миттєвого виклику
    (lambda : print("IIFE"))()
    print(oper( lambda x , y : x + y))
    print(oper( lambda x , y : x - y))
    hw()

if __name__ == '__main__' : main()
