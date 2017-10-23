#not working
def collatz(num):
    if (num%2 == 0):
        return num//2
    
    else:
        return 3*num + 1

def init(n):
    
    print("enter number please:")
    try:
        n = input()
        
    
    except NameError:
        init(n)
    
    #print (n)
    return n


#program
num = 0
num = init(num)
#print num

while(num>1):
    num = collatz(num)
    print (num)
    
        