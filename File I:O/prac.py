# Question :Create a new file "practice.text" using python. Add the following data in it :
'''
Hi everyone
we are learning File I/O
using python
I like programming in python
'''

#answer 

'''
with open ("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/practise.text","a+") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing python\nI like programming in python")
    f.close()
'''    

# QUESTION : WAF that replaces all occurrences of "Python" with "java" in above file 

'''
with open ("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/practise.text","r") as f:
    data = f.read()
    

new_data = data.replace("python","java")
print(new_data)

with open ("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/practise.text","w") as f:
    f.write(new_data)
    print(new_data)
    '''

# Question : Search if the word "learning" exists in the file or not.

# answer
'''
def check_for_word():
word = "learning"
with open("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/practise.text","r") as f:
    data = f.read()

    if(data.find(word) != "pypypy"):
        print("found")
    else:
        print("not found")
'''

# WAF to find in which line of the file does the word "learning" occur first. print -1 if word not found
        
# answer
'''
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/practise.text","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1       

check_for_line()
'''



    





