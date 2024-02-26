# using syntax to open a file and to read write e.t.c

# syntax : with open("fime name ","mode") as of f: # this is just a syntax and last as "f" means our selected any name 


with open("/Users/dhurwahidquadri/Documents/CWH-PY/File I:O/doc.txt","r+") as f :
    x = f.read()
    print(x)