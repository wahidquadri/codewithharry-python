# WAP to ask the user to enter names of their 3 favorite movies and store them in a list

'''movies = []
a = input("first movie is :")
b = input("second movie is :")
c = input("third movie is :")

movies.append(a)
movies.append(b)
movies.append(c)

print(movies)'''

# important point : palindrome means a both lists are same after doing reverse() then its palindrome or else if its different then its not a palindrome.
# QUE : wap a program to check if a list contains a palindrome of elements.(Hint : use copy()method)

'''this below code is related to palindrome

l = [1,2,3,2,1]
print(l.copy())
print(l.reverse())'''

# another method to know its a palindrome or not

'''l1 = [1,2,3,2,1]

x = l1.copy()
x.reverse()

if(x == l1):
    print("palindrome")
else:
    print("not palindrome")'''

# WAP to count the number of students with the "A" grade in the following tuple.("C","D","A","A","B","B","A")

'''t = ("C","D","A","A","B","B","A")
print(t.count("A"))'''  # O/P : 3

# STORE the above values in a list & sort them from "A" to "D" ?

grades = ["C","D","A","A","B","B","A"]
grades.sort()
print(grades)



