import pandas as pd

# DataFrame
df = pd.DataFrame({'Student Names' : ['Jenny', 'Singh', 'Charles', 'Richard', 'Veena'],
                   'Category' : ['Online', 'Offline', 'Offline', 'Offline', 'Online'],
                   'Gender' : ['Female', 'Male', 'Male', 'Male', 'Female'],
                  'Courses': ['Java', 'Spark', 'PySpark','Hadoop','C'],
                   'Fee': [15000, 17000, 27000, 29000, 12000],
                   'Discount': [1100, 800, 1000, 1600, 600]})
print(df)
print('-'*50)
pv = pd.pivot_table(df, index=['Category'],columns=['Courses'], values=['Fee'])

print(pv)

print('-'*50)


pv = pd.pivot_table(df, index=['Category'], columns=['Gender'],values=['Discount'], aggfunc=['mean'])
print(pv)
