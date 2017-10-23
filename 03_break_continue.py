while True:
    print('Please enter username:')
    name = raw_input()
    
    if (name != 'John'):
        continue
    
    print('Hi John, please enter password:')
    password = raw_input()
    if (password == 'python'):
        break
    print('Incorrect password')
    
print('Access Granted')