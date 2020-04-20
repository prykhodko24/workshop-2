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
for row in cursor:
    print(row)
print('\n')


query2 = '''SELECT COUNT(store_number) AS procent,ownership_type
FROM stores
group by ownership_type '''
cursor.execute(query2)
for row in cursor:
    print(row)
print('\n')

query3 = '''SELECT longitude,latitude
FROM Stores
WHERE brand_name='Teavana' '''
cursor.execute(query3)
for row in cursor:
    print(row)
cursor.close()
connection.close()
