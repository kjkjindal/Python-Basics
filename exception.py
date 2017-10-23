def div(num):
    try:                         #try a given set of statements
        return 42/num
    
    except ZeroDivisionError:    #if any of the statements shor the here mentioned error, execute the following code
        print('Cannot divide by Zero')
        

print(div(3))
print(div(0))