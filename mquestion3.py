f=open("file-question3.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i+=1
print(f)
    
    
    