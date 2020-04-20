import cx_Oracle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard




username = 'MYONLINEEDU'
password = 'njvf24'
databaseName = 'localhost/xe'
chart_studio.tools.set_credentials_file(username='t.prykhodko',api_key='5QCDRot27p6rJ3XQjSs4')
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()

def fileId_from_url(url):
    url_raw = url.split('/')
    cleared = [s.strip('~') for s in url_raw]  # remove the ~
    nickname = cleared[3]
    id = cleared[4]
    fileId = nickname + ':' + id
    return fileId


#---q1
query1 = """select uu.country, uu.cnt
from(
    SELECT country ,count(*) as cnt
    FROM Stores
    GROUP BY country
    ORDER BY count(*) desc
) uu
where rownum < 3"""
cursor.execute(query1)

num= list()
country = list()

for ownership_type, numb in cursor:
    print(numb)
    print(ownership_type)
    num.append(numb)
    country.append(ownership_type)
print("QUERY 1")
print(num)
print(country)
print('\n')
#--end q1--
#---q2--
query2 = '''SELECT COUNT(store_number) AS procent,ownership_type
FROM stores
group by ownership_type'''
cursor.execute(query2)
proc = list()
ownersh = list()

for procent, ownership_type in cursor:
    proc.append(procent)
    ownersh.append(ownership_type)
print('QUERY 2')
print(proc)
print(ownersh)
print('\n')
#---end q2---
query3 = '''SELECT brand_name, COUNT(*)
FROM Stores
GROUP BY brand_name
'''
cursor.execute(query3)
lati= list()
longit = list()

for brand_name, cnt in cursor:
    longit.append(brand_name)
    lati.append(cnt)
print('QUERY 3')
print(lati)
print(longit)
#---end q3
#---graph--
bar = go.Bar(
    x=country,
    y=num
)
gr_q1 = py.plot([bar], auto_open=False, filename='task 1')

pie = go.Pie(
    labels=ownersh,
    values=proc
)
gr_q2 = py.plot([pie], auto_open=False, filename='task 2')

scatter = go.Scatter(
    x=longit,
    y=lati
)
gr_q3 = py.plot([scatter], auto_open=False, filename='task 3')

#---end graph--

my_board = dashboard.Dashboard()
box1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(gr_q1),
    'title': '1 запит-кількість філіалів  в 3 країнах з найбільшої кількістю закладів '
}
box2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(gr_q2),
    'title': '2 запит-форми власності та відсоток закладів з такою формою власності',

}
box3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(gr_q3),
    'title': '3 запит-кількість філіалів у кожного бренду'
}

my_board.insert(box1)
my_board.insert(box2, 'below', 1)
my_board.insert(box3, 'right', 2)

py.dashboard_ops.upload(my_board, 'Tanya')


cursor.close()
connection.close()
