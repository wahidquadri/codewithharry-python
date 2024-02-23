'''dict = {
    "name" : "vahid",
    "Age" : 24,
    "CGPA" : 9.5,
    "subjects" : ["eng","tel","cse"],
    "marks" : (87,88,89)
}'''

# print(type(dict))

# print(dict["name"])  it will print the value of that name
# print(dict["Age"])   it will print the value of age
# print(dict["CGPA"])  it will print the value of CGPA
# print(dict["marks"]) it will print the value of marks

# >>>> TO modify in dict this process we will do <<<<<<<<<<<<

# to modity the value
'''dict["marks"] = (95,97,99)
print(dict)'''

#to add the value
'''dict["school"] = "pro stack"
print(dict) '''


#  >>>>>>  nested dictionary <<<<<<
'''student = {
    "name" : "wahid",
    "subjects" : {
        "eng" : 95,
        "hin" : 99,
        "CSE" : 100
    }
}'''

'''print(student)   # this will print all the dictionary
print(student["subjects"])  # this will print the selected part only i mean subjects only 
print(student["subjects"]["CSE"]) #ths will print the selected part such as in a dictionary select subjects and then in that select CSE subject so it will print only the CSE subject score 
'''

# >>> Dict methods <<<

mydict = {
    "name" : "vahid",
    "Age" : 24,
    "CGPA" : 9.5,
    "subjects" : ["eng","tel","cse"],
    "marks" : (87,88,89)
}

# important methods

'''mydict.keys()
mydict.values()
mydict.items()
mydict.get()
mydict.update()'''

'''print(list(mydict))     # all the dict keys shown in a list type
print(mydict.keys())       #  it prints all the keys names in the dict
print(mydict.get["name"])  #  it prints the selected key values in the dict
print(mydict.values())     #  it prints all the values in the given dict
print(mydict.items())      #  it prints all the (keys & values) in a tuples way of the given dict 
print(mydict.update({"Age" : 20})) # this will update the age value i mean replace the new value but cant add seperatly age again because keys are unique in dict and no dubplicate keys are allowed 
print(mydict.update({"city" : "Bangalore"}))  # it will add the new key and values in the above dict
we can add the key and value in a other way also see below code its another method to add
mydict["gender"] = "male"
print(mydict)'''







