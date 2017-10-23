#using list for repeated inputs

l = []

while True:
    print("Enter name of cat or type 'end' to exit")
    name = raw_input()
    if name == 'end':
        break
    
    l.append(name)

print("Cat names are:")

for i in l:
    print(i)