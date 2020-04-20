import cx_Oracle
import plotly.plotly as py
import plotly.graph_objs as go
import re
import plotly.dashboard_objs as dashboard


username = 'SYSTEM'
password = 'njvf24'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()


query1 = '''
select count(store_number) AS numb,country
from Stores
group by country
order by count(store_number) desc
fetch first 3 rows only'''
cursor.execute(query1)

num= list()
country = list()

for numb, ownership_type in cursor:
    num.append(numb)
    country.append(country)

data = [go.Bar(
            x=country,
            y=num
    )]
graph_1 = py.plot([bar], auto_open= False, filename='task 1')
#----------------------------------------------
query2 = '''SELECT
 COUNT(store_number) AS procent,ownership_type
FROM stores
group by ownership_type '''
cursor.execute(query2)

proc = list()
ownersh = list()

for procent, ownership_type in cursor:
    proc.append(procent)
    ownersh.append(ownership_type)

pie = go.Pie(labels=proc, values=ownersh)
graph_2= py.plot([pie], filename='task 2')
#----------------------------------------
query3 = '''SELECT longitude,latitude
FROM Stores
WHERE brand_name='Teavana' '''
cursor.execute(query3)
lati= list()
longit = list()

for longitude, latitude in cursor:
    longit.append(longitude)
    lati.append(latitude)

scatter = go.Scatter(
    x = lati,
    y = longit
    )

graph_3 = py.plot([scatter], auto_open= False, filename='task 3')


cursor.close()
connection.close()
#_____________________________________________________________
my_dboard = dashboard.Dashboard()

g1 = fileId_from_url(graph_1)
g2 = fileId_from_url(graph_2)
g3 = fileId_from_url(graph_3)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': g1,
    'title': 'Кількість філіалів в країні'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': g2,
    'title': 'Ввідсоток кожної ліцензій'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': g3,
    'title': 'розташування закладів з брендом Teavana'
 '
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Prykhodko')

