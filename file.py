

f=open("python.txt","w")
data=f.write("hrami")
print(data)
f.close

f=open("python.txt","r")
data=f.read()
print(data)
f.close