car = {'color':'red', 'speed':50, 'year': 2017, 'company': 'BMW'}


#gets keys
for i in car:
    print i
   
print ""

#gets values
for i in car.values():
    print i
    
print ""

#gets keys
for i in car.keys():
    print i
    
print ""

#gets both keys and values as tuples
for i in car.items():
    print i
    
print ("enter key name")
name = raw_input()

if (name in car):   #or name in car.keys()
    print ("present!")
    
else:
    print ("no!")