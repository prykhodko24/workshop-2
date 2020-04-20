import cx_Oracle
username = 'SYSTEM'
password = 'njvf24'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()


query1 = '''SELECT COUNT(store_number),country
FROM Stores
GROUP BY country
ORDER BY count(store_number) desc
fetch first 3 rows only '''
cursor.execute(query1)
proc = list()
ownersh = list()

num= list()
country = list()

for numb, ownership_type in cursor:
    num.append(numb)
    country.append(country)
print(num)
print(country)
print('\n')


query2 = '''SELECT COUNT(store_number) AS procent,ownership_type
FROM stores
group by ownership_type '''
cursor.execute(query2)
proc = list()
ownersh = list()

for procent, ownership_type in cursor:
    proc.append(procent)
    ownersh.append(ownership_type)
print(proc)
print(ownersh)
print('\n')

query3 = '''SELECT longitude,latitude
FROM Stores
WHERE brand_name='Teavana' '''
cursor.execute(query3)
lati= list()
longit = list()

for longitude, latitude in cursor:
    longit.append(longitude)
    lati.append(latitude)
print(lati)
print(longit)
cursor.close()
connection.close()
