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

result = pd.pivot_table(
        df,
        values = "Salary",
        index = "City",
        aggfunc = "mean"
)
print(result)

result_a = pd.pivot_table(
        df,
        values = "Salary",
        index = "City",
        aggfunc = "max"
)
print(result_a)

employees = pd.DataFrame({
    "EmployeeID": [1, 2, 3, 4],
    "Name": ["John", "Alice", "Bob", "David"],
    "DeptID": [10, 20, 10, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 30],
    "Department": ["IT", "HR", "Finance"]
})

result_b = pd.merge(
       departments,
       employees,
       on = "DeptID",
       how = "inner"
)
print(result_b)

result_c = pd.merge(
       departments,
       employees,
       on = "DeptID",
       how = "left"   
)
print(result_c)

employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["John", "Alice", "Bob", "David", "Emma"],
    "dept_id": [10, 20, 30, 40, 50],
    "salary": [50000, 60000, 45000, 70000, 55000]
})

df1 = pd.DataFrame(employees)
print(df1)

departments = pd.DataFrame({
    "dept_id": [10, 20, 30, 40, 60],
    "department": ["HR", "IT", "Sales", "Finance", "Marketing"],
    "location": ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Pune"]
})

df2 = pd.DataFrame(departments)


result_d = pd.concat([df1,df2],ignore_index = True)
print(result_d) 

result_e = pd.concat([df1,df2],axis = 1)
print(result_e)

dates = pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "JoiningDate": ["2024-01-15", "2023-06-20", "2025-03-10"], 
    "Salary": [50000, 60000, 45000,],   
    "City": ["Hyderabad", "Delhi", "Mumbai"]
})


dates["JoiningDate"] =  pd.to_datetime(dates["JoiningDate"])
print(dates)

dates["year"] = dates["JoiningDate"].dt.year
print(dates)

dates["month"] = dates["JoiningDate"].dt.month
print(dates)

dates["day"] = dates["JoiningDate"].dt.day
print(dates)

result_f = dates[dates["JoiningDate"] > "2024-01-01"]
print(result_f)

df["City_Avg_Salary"] = df.groupby("City")["Salary"].transform("mean")
print(df)

df = df.drop_duplicates(
    subset=["Name"],
    keep="first"
)
print(df)