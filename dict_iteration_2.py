x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:   #iterate through the keys
    print(i)  #returns each keys





x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x.keys():    #iterate through the keys
    print(i)          #returns each keys






x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x.values():      #iterate through the values
    print(i)              #returns each values




 
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i,j in x.items():
    print(i,j)      #return both values and keys just like a tuple
