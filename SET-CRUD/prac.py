# Question 1

'''Store following word meanings in a python dictionary and print only table
table : "a piece of furniture","list of facts and figures"
cat : "a cute pet" '''

'''dict = {
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat" :  "a cute pet"
}

print(dict["table"]) # it will print only table 
print(dict) # it will print all dict values'''

# Question 2

# you are given a list of subjects for students assume one classroom is required for one subject how many classrooms are needed by all students.
# "python","java","C++","python","javascript","java","python","java","C++","C"
'''
sub = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(sub))
print(sub)
'''

# Question 3

'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
  start with an empty dictionary & add one by one ,use subject name as key & marks as values'''

'''dict = {}

sub1 = int(input("maths marks :"))
dict.update({"maths" : sub1})

sub2 = int(input("physics marks :"))
dict.update({"physics" : sub2})

sub3 = int(input("chemistry marks :"))
dict.update({"chemistry" : sub3})

print(dict)'''

# Question 4

'''Figure out a way 9 & 9.0 as seprate values in the set.
(you can take help of build-in data types)'''

'''if we do like this it will print only 9 because both 9 and 9.0 are same 
s1 = {9,9.0}
print(s1)'''

#another way to do this above answer

s1 = {
    ("float", 9.0),
    ("int", 9)
}
print(s1)
print(type(s1))












