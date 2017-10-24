#maintaining and updating databses is easy wih dictionaries

dict = {'Alice':'Apr 1', 'Bob': 'Feb 23', 'Joe': 'May 11'}

while True:
    print("Enter name(blank to quit)")
    name = raw_input()
    
    if (name == ''):
        break
    
    if name in dict:
        print("Your birthday is on " +dict[name])
        
    else:
        print("Name not in database, please type your birth date in Mmm dd format (blank to quit):")
        date = raw_input()
        
        if (date == ''):
            break
        
        dict[name] = date
        print ("Database updated")
    

#database is reset to original state once the program exits

        