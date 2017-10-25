count = {}

while True:
    print ("Enter string (or blank to exit)")
    s = raw_input()
    s = s.lower()
    
    if (s == ''):
        break
    
    for c in s:
        count.setdefault(c, 0)
        count[c] +=1
    
    print (count)
    
    count.clear()