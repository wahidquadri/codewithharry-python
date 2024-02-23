# SET CRUD OPERATIONS

s1 = {} # this will be a <dict type> because its an empyt set{}
s2 = {10,"vahid",20} # it will be <set type> only because values are present in set{} 

s = {20,30,"vahid",30.5,"khan"}
'''print(len(s))
print(type(s1))
'''


# SET Methods
'''s.add(True) # it will add the value in the above set
s.remove(30.5) # it will remove the certain given value in the above list 
s.clear()      # it will clear all the values given in the set and then it will be empty {}
s.pop()        # it will remove anyone random value in the given set
'''

# SET METHODS UNION ANSD INTERSECTION
# set1.union(set2) in the both set1 and set2 values those are unique it will print
# set1.intersection(set2) in the both set1 and set2  those are common or similar that will be print

set1 = {10,20,30,40,50}
set2 = {30,10,60,70,20}

x = set1.union(set2)        # in the both set1 and set2 values those are unique it will print
y = set1.intersection(set2) # in the both set1 and set2  those are common or similar that will be print

print(x)
print(y)








