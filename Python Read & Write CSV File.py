import pandas as pd

#Skip the first 2 rows.
#df=pd.read_csv("EmpData.csv",skiprows=2)

#Header is located at Row Number 1. Also, Index start from 0.
#df=pd.read_csv("EmpData.csv",header=1)

#If we don't have header we can set the Header to None it will add the indexes like 0,1 2,3 to header or we can also add the names of header in sequance as we added already in this line.
#df=pd.read_csv("EmpData.csv",header=None, names=["id","name","designation","salary","joining date"])
#print(df)

#Read Limited Data From CSV File
# df=pd.read_csv("EmpData.csv",nrows=2)
# print(df)

#CleanUP Messsy Data From File. This will replace na or NX with NaN as it helps us cleaning data from file
# df=pd.read_csv("EmpData.csv",nrows=4,na_values=["na","NA"])
# print(df)
#
# #Writing To CSV File and index=False is to not write the index to the csv file
# df.to_csv("new.csv",index=False,columns=["ID","Name","Salary"])

#Write CSV File Using Pandas
name=["Kaif","Mic"]
deg=["BSCS","BSIT"]
dict={"Name":name,"Degree":deg}
df=pd.DataFrame(dict)
df.to_csv("new.csv",index=False)