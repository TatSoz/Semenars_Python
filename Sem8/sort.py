import pandas as pd

def sort_data():
    bd = pd.read_csv('employees.csv')
    bd = bd.sort_values('ID', ascending=True)
    bd.reset_index(drop=True, inplace=True)
    print(bd)
    bd.to_csv('sort.csv', index=False)




