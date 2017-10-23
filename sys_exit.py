import sys

count = 0
while True:
    print('Please enter username:')
    name = raw_input()
    
    if (name != 'John'):
        continue
    
    print('Hi John, please enter password:')
    password = raw_input()
    
    if (count>=5):
        print('Too many wrong attempts, exiting')   #worng passowrd tolerance: 6 times
        sys.exit()
    
    if (password == 'python'):
        break
    
    print('Incorrect password')
    #print (count)
    count = count + 1
    
print('Access Granted')