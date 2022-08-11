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
print()
print(qq)
print(pp)
file3.close()

filename3=open("filename3.txt","r")
print("The filepointer is at byte before reading the file :",filename3.tell())
content = filename3.readlines()
print(content)
print("The filepointer is at byte after reading the file :",filename3.tell())
filename3.close()

print("FileName 3 using read")
filenamee=open("filename3.txt","r+")
content= filenamee.readlines()
print(content)
filenamee.write("AlexSmith is great person")
filename3.close()


dataa=open("studentname.txt","r")
print("The filepointer is at byte: ",dataa.tell())
dataa.seek(20) #Change the current file position to 20, and return the rest of the line
print("The filepointer is at byte: ",dataa.tell())
print(dataa.read())
dataa.close()
#
# import subprocess #In Python, there are the requirements to write the output of a Python script to a file so the prcess and the code is given below:
# #file.py code:
# temperatures=[10,-20,-289,100]
# def c_to_f(c):
#     if c< -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f=c*9/5+32
#         return f
# for t in temperatures:
#     print(c_to_f(t))
# file.py:
# with open("output.txt", "wb") as f:
#     subprocess.check_call(["python", "file.py"], stdout=f)

# stunaame=open("studentname.txt","x")
# if stunaame:
#     print("File Created")



