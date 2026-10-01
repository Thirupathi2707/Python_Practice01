import pandas as pd

df = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112],
    
    "Name": ["John", "Alice", "Bob", "David", "Emma", "John",
             "Mike", "Sarah", "Tom", "Priya", "Raj", "Anu"],
    
    "Age": [25, 30, 22, 35, 28, 25, 32, 27, 40, 29, 31, 24],
    
    "Salary": [50000, 60000, 45000, 80000, 55000, 50000,
               70000, 52000, 90000, 58000, 65000, 48000],
    
    "City": ["Hyderabad", "Delhi", "Mumbai", "Hyderabad", "Chennai",
             "Hyderabad", "Delhi", "Mumbai", "Hyderabad", "Chennai",
             "Delhi", "Hyderabad"],
    
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT",
                   "Finance", "IT", "Finance", "HR", "IT", "HR"],
    
    "JoiningDate": [
        "2022-01-15", "2023-06-20", "2021-03-10", "2024-01-05",
        "2023-11-12", "2022-01-15", "2020-07-25", "2024-05-18",
        "2019-09-30", "2023-06-20", "2021-12-10", "2024-08-15"
    ]
}
df = pd.DataFrame(df)

salary_series = pd.Series(df["Salary"])
print(salary_series)

print(df.head(5))
print(df.tail(3))
print(df.shape)
print(df.dtypes)
print(df[["Name","Salary","City"]])
print(df.iloc[3])
print(df[df["Salary"] > 60000])
result = df[df["City"].isin(["Hyderabad","Delhi"])]
print(result)
print(df[(df["Age"] > 25) & (df["Age"] < 35)])
df["bonus"] = df["Salary"] * 0.1
print(df)
df["Experience"] = df["Age"].apply(
    lambda Age : "Experienced" if Age >= 30 else "Beginner"
)
print(df)
df["City"] = df["City"].str.upper()
print(df)
result_a = df["Salary"].max()
print(result_a)

df = df.sort_values("Salary",ascending = False)
print(df)

df = df.sort_values(by = ["Department","Salary"],ascending = [True,False])
print(df)

print(df.isna())

df["Salary"] = df["Salary"].fillna(0)
print(df)

print(df.dropna())

print(df.duplicated().sum())

print(df.drop_duplicates())

df["avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
print(df)

df["total_salary"] = df.groupby("City")["Salary"].transform("sum")
print(df)

print(df.groupby("Department").size())

#Find the minimum, maximum, and average salary for each Department using agg().

result_c = df.groupby("Department").agg({"Salary":["max","min","mean"]})
print(result_c)

#Find the average age and average salary for each City.

result_d = df.groupby("City").agg({"Salary": "mean","Age": "mean"})
print(result_d)

def salary_in_thousands(salary) :
        return salary/1000

df["Salary_k"] = df["Salary"].apply(salary_in_thousands)
print(df)

def age_cat(age):
        
        if age < 25:
            return "Young"
        elif age >= 35:
            return "Senior"
        else :
           return "Adult"
        
df["Age_Group"] = df["Age"].apply(age_cat)
print(df)

#Create a pivot table showing the average salary for each Department.
     
result_e = pd.pivot_table(
      df,
      values = "Salary",
      index = "Department",
      aggfunc = "mean"       
)
print(result_e)

#Create a pivot table showing the average salary by City and Department.

result_f = pd.pivot_table(
     df,
     values = "Salary",
     index = ["City","Department"],
     aggfunc = "mean"
)
print(result_f)


employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["John", "Alice", "Bob", "David", "Emma"],
    "Age": [25, 30, 22, 35, 28],
    "Salary": [50000, 60000, 45000, 80000, 55000],
    "DepartmentID": [1, 2, 1, 3, 2]
})

print(employees)

departments = pd.DataFrame({
    "DepartmentID": [1, 2, 3],
    "Department": ["IT", "HR", "Finance"],
    "Location": ["Hyderabad", "Delhi", "Mumbai"]
})

print(departments) 

result_g = pd.merge(
      employees,
      departments,
      on = "DepartmentID",
)
print(result_g)

result_h = pd.merge(
     employees,
     departments,
     on = "DepartmentID",
     how = "left"
)
print(result_h)