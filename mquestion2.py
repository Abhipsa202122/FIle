f=open("people-exercise.txt")
data=f.read()
print(data)
f.close()
i=0
c=0
while i<len(data):
    if data[i]=="\n":
        c+=1
    i+=1
print(c)   
    

