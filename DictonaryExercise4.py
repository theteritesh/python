# Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

d=dict.fromkeys(employees,defaults)
print(d)