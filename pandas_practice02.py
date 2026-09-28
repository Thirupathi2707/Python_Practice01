import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "David", "Emma", "John",
             "Mike", "Sarah", "Tom", "Priya"],
    
    "Age": [25, 30, 22, 35, 28, 25,
            32, 27, 40, 29],
    
    "Salary": [50000, 60000, 45000, 80000, 55000, 50000,
               70000, 52000, 90000, 58000],
    
    "City": ["Hyderabad", "Delhi", "Mumbai", "Hyderabad", "Chennai",
             "Hyderabad", "Delhi", "Mumbai", "Hyderabad", "Chennai"]
}

df = pd.DataFrame(data)

print(df)

df["avg_salary"] = df.groupby("City")["Salary"].transform("mean")
print(df)

df["total_salary"] = df.groupby("City")["Salary"].transform("sum")
print(df)

print(df.groupby("City").size())

df["maxim_salary"] = df.groupby("City")["Salary"].transform("max")
print(df)

result = df.groupby("City").agg({ "Salary":["max","min"]})
print(result)

result = df.groupby("City").agg({"Salary": "mean","Age": "mean"})
print(result)

df["Experience"] = df["Age"].apply(
    lambda Age: "Experienced" if Age >= 30 else "Beginner"
)
print(df)

def salary_in_thousands(salary):
            return salary/1000
df["Salary_K"] = df["Salary"].apply(salary_in_thousands)
print(df)

def Category(sal):
        if sal >= 60000:
            return "High"
        else:
            return "Low"

df["Salary_cat"] = df["Salary"].apply(Category)
print(df)