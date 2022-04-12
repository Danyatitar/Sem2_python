import module1 as f
print("input name of file")
name=input()
text=[]
text=f.inputInFile(name)
text=f.process(text)
f.toNewFile(name,text)
print()
f.out(name)




