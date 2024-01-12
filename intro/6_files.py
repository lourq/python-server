
def crete_file1() -> None : 
    filename = "file1.txt"
    file = None
    try :
        file = open(filename , mode='w',encoding="utf-8")
        file.write("Latin data\n")
        file.write('Some Data')
    except OSError as err : 
        print(err)
    else : 
        file.flush() # для принудительной записи данных , которые находятся в буфере
        print("Create OK")
    finally : 
        if file != None : file.close()

def read_all_text1(filename:str) -> str : 
    file = None
    try :
        file = open(filename , mode='r')
    except OSError as err : 
        print(err)
    else : 
        return file.read()
    finally : 
        if file != None : file.close()

def create_headers(filename:str) -> None :
    try : 
        with open( filename , mode='w' , encoding='utf-8') as file :
            file.write( "Host: localhost\r\n" )
            file.write( "Connection: close\r\n" )
            file.write( "Content-Type: text/css\r\n" )
            file.write( "Content-Length: 100500\r\n" )
    except IOError as err : 
        print("Create headers error:" , err)
    else : 
        print("Create headers OK") 

def print_headers( filename:str) :
    try : 
        with open(filename , mode='r' , encoding='utf-8') as file : # автоматично закриває файл після завершення роботи з ним
            n = 1
            for x in file : 
                print( n , x)
                n += 1
                # Ітерування файлу: відбувається по рядках, але
                # символи \г\й сприймаються як два рядки
                # А також кінцевий символ переведення рядка 
                # включається до самого "x"
    except IOError as err :
        print(err)

def parse_headers(filename:str) -> dict | None:
    '''
        Розбирає файл "filename" i повертає dict
        з розділеними заголовками на ключі та значення
    '''
    # ret = {} # {} - dict
    try : 
        with open( filename , mode='r' , encoding='utf-8') as file :
            # for line in file :
            #     if ':' in line : 
            #         k , v = line.split(':')
            #         ret[k.strip()]= v.strip() # ~ trim()
        # return ret
            return { k : v 
                for k , v in (
                    map(str.strip , line.split(':'))
                        for line in 
                        file.readlines()
                        if ':' in line
                )}
        # Функціональний підхід - у застосуванні
        # генераторів - "ледачіх" алгоритмів
        # формування даних. Це дозволяє працювати
        # 3 Big Data
        # умова фільтрації може додаватись до генератора
    except IOError as err :
        print(err)
        return None

def main() -> None :
    # crete_file1()
    # print(read_all_text1('file1.txt'))
    # create_headers('headers.txt')
    # print_headers('headers.txt')
    for k , v in parse_headers('headers.txt').items() :
        print(k , v)

if __name__ == '__main__' : main()