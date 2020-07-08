x = [('one',1),('two',2),('three',3),('four',4),('five',5)]
y = dict(x)
print(y.get('six'))    #.get retuns None, if it's not in the list
print(y.get('six',"The key isn't in the dict"))   #.get retuns the 2nd argument, if it's not in the list
