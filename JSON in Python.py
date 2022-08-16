import json

#Python Convert to JSON string. Convert dictionary to JSON. json.dumps() method can convert a Python object into a JSON string and json.dump() method can be used for writing to JSON file.
stud={"Name":"Alex","Class":"BSCS","Grade":"A","Subjects":["Cs","SE","IT"]}
with open("Data.json","w") as file:
    json.dump(stud,file)
with open("Data.json","r") as fil:
    data=json.load(fil)
    print(data)
#Dumps Function and #Python pretty print JSON. To analyze and debug JSON data, we may need to print it in a more readable format. This can be done by passing additional parameters indent and sort_keys to json.dumps() and json.dump() method.
dat={"ID":"1","Model":"Apple","Price":"$2200"}
r=json.dumps(dat,indent=4,sort_keys=True)
print(r)

#JSON Data Convert to Python
student= {"Name": "Peter","Roll_no": "0090014","Grade": "A","Age":20}
with open("filestudent.json","w") as fi:
    json.dump(student,fi)
with open("filestudent.json","r") as f:
     dat=json.load(f)
     print(dat)

dt={"ID":"2","Model":"Samsung","Price":"$1200"}
rr=json.dumps(dt,indent=4,sort_keys=True)
print(rr)

cc=json.loads(rr)
print(cc)