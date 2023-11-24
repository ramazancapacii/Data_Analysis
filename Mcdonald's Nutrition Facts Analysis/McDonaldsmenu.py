

import pyodbc
import pandas as pd
import pandas as pd
pd.set_option('display.max_rows', None)  # maksimum satır sayısını sınırsız olarak ayarlar
pd.set_option('display.max_columns', None)  # maksimum sütun sayısını sınırsız olarak ayarlar
pd.set_option('display.width', None)  # çıktı genişliğini sınırsız olarak ayarlar
pd.set_option('display.max_colwidth', None)  # sütun genişliğini sınırsız olarak ayarlar


#Windows Authentication
db = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=localhost;'
    'Database=McDonalds;'
    'Trusted_Connection=True;'
)

# Bağlantıyı kullanarak bir sorgu yapabilirsiniz
cursor = db.cursor()
cursor.execute('SELECT * FROM menu')

# Sonuçları almak için fetchall() yöntemini kullanabilirsiniz
results = cursor.fetchall()

# SQL den alınan verileri DataFrame olarak atıp daha kolay analiz etmemize yarar.
df2 = pd.read_sql_query("select * from menu;", db)

df2.head()
# temel istatistikleri görüntülüyoruz 
df2.describe(include='all')

#Veri görselleştirme için kütüphaneleri import ediyoruz.
import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns 

#Sodium miktarını görselleştirdik.
plot = sns.swarmplot (x='Category', y='Sodium', data=df2)
plt.setp(plot.get_xticklabels(), rotation=70)
plt.title('Sodium Content')
plt.show()

#Sodiumun temel istatistiklerini getirelim
df2['Sodium'].describe()

#Sodiumun maksimum olduğu index 
df2['Sodium'].idxmax()

#Proteinli besinlerin görselleştirilmesi 
 
plot = sns.jointplot (x='Protein', y='Total Fat', Data=df2)
plot.show()

#Seker değerini  görselleştireceğiz
plot=sns.set_style('whitegrid')
ax = sns.boxplot(x=df2['Sugars'])
plot.show()
# Bağlantıyı kapatın
db.close()
