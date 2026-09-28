import pandas as pd

s = pd.Series([10,20,30],
                index=["john","alice","bob"])

print(s)

data = {
    "name" : ["john","alice","bob"],
     "age" : [25,26,28],
     "Salary":[50000,60000,70000]
}

df =  pd.DataFrame(data)

print(df)

print(df.head(1)) 
print(df.tail(1))
print(df.info())
print(df.dtypes)
print(df.describe())
print(df["name"])
print(df.shape)
print(df.duplicated())
print(df.duplicated().sum())
print(df.isnull())
print(df.isnull().sum())
print(df[["name","Salary"]])
print(df.iloc[1])
print(df.iloc[0:2])
print(df.loc[0,"name"])
print(df[df["age"]>25])
print(df[(df["age"] > 25) & (df["Salary"] > 50000)])
df["bonus"] = 5000

print(df)

df["new salary"] = df["Salary"] + 10000

print(df)

df = df.sort_values("Salary",ascending = False)
print(df)

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "David", "Emma", "John"],
    "Age": [25, 30, 22, 35, 28, 25],
    "Salary": [50000, 60000, 45000, 80000, 55000, 50000],
    "City": ["Hyderabad", "Delhi", "Mumbai", "Hyderabad", "Chennai", "Hyderabad"]
}

df = pd.DataFrame(data)

print(df)
print(df.head(3))
print(df.tail(2))
print(df["Name"])
print(df[["Name","Salary"]])
print(df.iloc[2])
print(df.iloc[0:3])
print("rows:",df.shape[0])
print("columns:",df.shape[1])
print(df.dtypes)
print(df.info())
print(df[df["Salary"] > 55000])
print(df[df["Age"] < 30])
print(df[(df["Salary"] > 50000) & (df["Age"] > 25)])
result = df[df["City"].isin(["Hyderabad","Delhi"])]
print(result)

df["Bonus"] = 0.1 * df["Salary"]
print(df)

df = df.sort_values("Salary", ascending = False)
print(df)

print(df.duplicated().sum())

df = df.drop_duplicates()
print(df)

mean_salary = df["Salary"].mean()
print("mean salary: ",mean_salary)

df["Experience"] = df["Age"].apply(
    lambda Age : "Experienced" if Age >= 30 else "Beginner"
)
print(df)

