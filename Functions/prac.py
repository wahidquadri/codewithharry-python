# WAF to print the length of the list. (list in parameter)

'''
Normal way to know the length of list

cities = ["mumbai", "pune", "chennai", "hyd"]
x = len(cities)
print(x)'''

# using funtion to know the length of the list
'''cities = ["mumbai", "pune", "chennai", "hyd"]
heroes = ["khan","kapoor","king"]

def print_length(x):
    print(len(x))

print_length(cities)    
print_length(heroes)'''

# WAF to print the elements of a list in a single line.(list is the parameter)
# normal way for the above question answer is :

'''cities = ["mumbai", "pune", "chennai", "hyd"]
heroes = ["khan","kapoor","king"]

print(heroes, end="  ")
print(cities)'''

#using function way is below answer 

'''
cities = ["mumbai", "pune", "chennai", "hyd"]
heroes = ["khan","kapoor","king"]

def mylist(x):
    for item in x:
        print(item, end=" ")

mylist(heroes)
mylist(cities)
print()'''


#WAF to find the factorial of n. (n is parameter)

'''def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)    '''

# Question : WAF to convert USD to INR.

'''def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =", inr_val, "INR")

convert(1)
convert(2)'''






