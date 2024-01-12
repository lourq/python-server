def main() -> None :
    try : 
        throw()
    except :
        print("Error detected")

    try :
        throw_msg()
    except TypeError : 
        print("TypeError detected")
    except ValueError as err :
        print("ValueError detected: " , err)
    except : 
        print( "Unknown error detected")
    finally :
        print( "Finally action")
    
    try : 
        no_throw()
    except : 
        print("Unknown error detected")
    else :
        print("Else action")
    finally : 
        print( "Finally action")

def throw() -> None : 
    print("Raising error")
    raise TypeError

def throw_msg() -> None :
    print("Raising message error")
    raise ValueError("The error message")

# y Python немає поняття порожнього блоку, типу {}
# якщо у блоці немає операцій, то використовується
# "заглушка" pass (NOP)


def no_throw() -> None : 
    pass

if __name__ == '__main__' : main()