l = ['john', 'zack', 'tim', 'joe', 'carl', 'zack']

print (l.index('zack'))  #first appearance

l.append('jim')
print (l)

l.insert(1, 'steve')
print (l)

l.remove('zack')   #first appearance removed
print (l)

l.sort()
print (l)

l.sort(reverse = True)
print (l)
a = l + [1,2,3]
a.sort()
print (a)  #integers given precedence

#copying from one list to another (not creating another reference)

import copy

l2 = copy.copy(l)
l2[1] = 100

print(l2)
print(l)