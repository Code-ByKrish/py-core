import pandas as pd 

data = {
    "Name" : ["Spongebob","Patrick","Squidward"], 
    "Age" : [30,35,50]
}

df = pd.DataFrame(data, index =["Employee 1","Employee 2","Employee 3"])
print(df)
print(df.loc["Employee 1"])
print(df.iloc[1])

#add a new column 
df["Job"] = ["Cook","N/A","Cashier"]
print(df)

#add a new rows
new_rows = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},
                        {"Name":"Leon","Age":55,"Job":" Special Agent"}],index = ["Employee 4","Employee 5"])
print(df)
df = pd.concat([df, new_rows])
print(df)