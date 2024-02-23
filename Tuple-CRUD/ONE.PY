
'''l = [10,20,"vahid"]
l[2]="shahid"              this is an replace the new value on the old value in a list 
print(l)'''

#  >>>>  Tuple CRUD operations  <<<<
t = (10,20,"vahid",True,"khan",[10,20,20,10])
x = list(t)
x.append("orange")
print(type(x))


print(x)



#  important points in  Tuple()

''' Ordered: >Tuples are part of sequence data types, which means they hold the order of the data insertion. 
    It maintains the index value for each item.

Unchangeable: >Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.

Heterogeneous: >Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) 
and can be accessed through indexing and slicing.

Contains Duplicates: >Tuples can contain duplicates, which means they can have items with the same value.'''

