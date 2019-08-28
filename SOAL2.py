import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'taikucing',
    database = 'world'
)

query1 = '''select country.Name as Negara_ASEAN, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from
country inner join city
on country.Capital = city.ID where country.Name = 'Brunei' or country.Name ='Cambodia' or country.Name ='East Timor' or country.Name ='Indonesia' or country.Name ='Laos' or country.Name ='Malaysia' or country.Name ='Myanmar' or country.Name ='Philippines'or country.Name ='Singapore' or country.Name ='Thailand' or country.Name ='Vietnam' order by country.Name asc'''

df = pd.read_sql(query1, con=db)
negara = list(df['Negara_ASEAN'])
populasi = list(df['Populasi_Negara'])

x= negara
y= populasi

#####   NO 1    ######
for a,b in zip(x,y):
    plt.text(a,b, str(b), ha='center', size=6)
plt.bar(x,y,color=['red','green','lavender','yellow','blue','lightblue','lightgreen','pink','magenta','purple','golderod'])
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi')
plt.xticks(rotation=45, size=6)
plt.grid(True)
plt.show()

# ######  NO 2 ######
color = ['red','blue','green','yellow','lightgreen','lightblue','pink','coral','aqua','lightgrey','lime']
plt.pie(
    y, labels=x, colors=color,
    startangle=360, counterclock=True,
    autopct='%1.1f%%',
    textprops={'color':'black'}
)
plt.show()


####    NO 3   #####
df = pd.read_sql(query1, con=db)
negara1 = list(df['Negara_ASEAN'])
gnp = list(df['GNP'])

x= negara1
y= gnp

for a,b in zip(x,y):
    plt.text(a,b, str(b), ha='center', size=6)
plt.bar(x,y,color=['red','green','fuchsia','yellow','blue','lightblue','lightgreen','pink','crimson','plum','orangered'])
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('GNP')
plt.xticks(rotation=45, size=6)
plt.grid(True)
plt.show()


####    NO 4   #####
query2 = '''select country.Name as Negara_ASEAN, country.SurfaceArea as LuasDaratan, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from
country inner join city
on country.Capital = city.ID where country.Name = 'Brunei' or country.Name ='Cambodia' or country.Name ='East Timor' or country.Name ='Indonesia' or country.Name ='Laos' or country.Name ='Malaysia' or country.Name ='Myanmar' or country.Name ='Philippines'or country.Name ='Singapore' or country.Name ='Thailand' or country.Name ='Vietnam' order by country.Name asc'''

df = pd.read_sql(query2, con=db)
negara2 = list(df['Negara_ASEAN'])
luas = list(df['LuasDaratan'])

x=negara2
y=luas

color = ['red','blue','green','tomato','lightgreen','teal','pink','purple','turquoise','wheat','yellowgreen']
plt.pie(
    y, labels=x, colors=color,
    startangle=360, counterclock=True,
    autopct='%1.1f%%',
    textprops={'color':'black'}
)
plt.show()