l = [1,2,3,4,5,6]

#l[1.0] is wrong
#l[1] is correct
#l[-1] is 6

print (l[0:3]) #ind 0,1,2
print (len(l))
print (l*3)  #3 repetitions of the list

del l[2]  #removes 3 from the list

print(list('hello'))

l2 = l
l3 = [1,2,3,4,5,6]

l[1] = "Hi"

print (l, l2, l3)

#l and l2 refer to the same object, hence both modified simultaneously, but not l3