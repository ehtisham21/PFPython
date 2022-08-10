file=open("filename.txt","r")
if file:
    print("File Opened Successfully")
file.close()

with open("filename.txt",'r') as f:
    content = f.read();
    print(content)
file1=open("filename1.txt","w")
file1.write('''Hello First Team how are you
            Thank you''')
file1.close()
file2=open("filename2.txt","a+")
file2.write("Good Morning\n")
file2.write("File 2\n")
file2.close()
file2=open("filename2.txt","r")
aa=file2.read()
print(aa)
file2.close()

file2=open("filename2.txt","r")
for i in file2:
    print(i)
file2.close()

file3=open("filename3.txt","r")
pp=file3.readline()
qq=file3.readline()
print(qq)
print(pp)
file3.close()

filename3=open("filename3.txt","r")
content = filename3.readlines()
print(content)
filename3.close()