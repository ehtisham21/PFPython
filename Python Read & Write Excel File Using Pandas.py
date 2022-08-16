import pandas as pd

# f=pd.read_excel("Data.xlsx",sheet_name="Sheet1")
# print(f)
#
# f.to_excel("newData.xlsx",sheet_name="StuData",index=False,startrow=3,startcol=3)

name=["Kaif","Mic"]
deg=["BSCS","BSIT"]
sec=["A","B"]
dict={"Name":name,"Degree":deg,"Section":sec}
f=pd.DataFrame(dict)
f.to_excel("newData.xlsx",sheet_name="StuData",index=False)