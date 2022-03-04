f=open("highest_word.txt","r")
# f.write("my NAme is ABHIpsha")
# f.close()
data=f.read()
print(data)
f.close()
# data="my name IS"
i=0
c=0
while i<len(data):
    if data[i]>="a"and data[i]<="z":
       c+=1
    i+=1
print(c)              