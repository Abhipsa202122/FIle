f=open("wordlen_3.txt","r")
#f.write("My name is Abhipsa \n")
#f.write("I am a student at Navgurukul\n")
#f.close()
data=f.read()
print(data)
f.close()
i=0
c=0
m=0
while i<len(data):
    if data[i]>m:
       m=data[i]
       c+=1
    i+=1
print(m,c)       
    
