def inputInFile(name):
    file=open(name+".txt",'w',encoding='utf-8')
    a=[]
    print("Input text, to end input Ctrl+X")
    line = input()
    while line != '\x18':
        a.append(line)
        file.write(line+'\n')
        line = input()
    file.close()
    return a
def process(a=[]):
    for i in range(len(a)):
       a[i]=str(len(a[i]))+" "+a[i]+" "+str(i+1)
    return a
def toNewFile(name, a=[]):
    file=open("New_" + name + ".txt",'w',encoding='utf-8')
    for i in range(len(a)):
        file.write(a[i]+'\n')
    file.close()
def out(name):
    file=open(name+".txt",'r',encoding='utf-8')
    Newfile=open("New_" + name + ".txt",'r',encoding='utf-8')
    print("First file")
    print(file.read())
    file.close()
    print()
    print("New file")
    print(Newfile.read())
    Newfile.close()