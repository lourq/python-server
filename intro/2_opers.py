# x = (1,'1')
x = 1
print(x , type(x))

# y = tuple('1212')
y = 2
print(y)

x , y = y , x # swap 
x , y = y , x + y # Фибоначчи

s = "Hello, %s!" % ("World")
s = "x = %d, y = %d" % (x , y)
s = f"x = {x} , y = {y}"    # императивный подход