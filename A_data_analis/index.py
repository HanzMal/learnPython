import pandas as pd
# memuat data bernama 'dataset_statistics.csv' dan memasukkan hasilnya ke dalam 'raw_data'
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print(raw_data)

# melihat 10 data pada baris pertama
print (raw_data.head(10))

# melihat 5 data pada baris terakhir
print (raw_data.tail())

# melihat dimensi dari raw_data
print (raw_data.shape)

# mengambil jumlah data
print (raw_data.shape[0])

# Untuk melihat kolom apa saja yang terdapat pada dataset cukup menggunakan method columns
print(raw_data.columns)

print (raw_data.isna())
print (raw_data.isna().sum())