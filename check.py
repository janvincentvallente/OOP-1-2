import pyodbc

msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS']
print(f'Access Drivers : {msa_drivers}')