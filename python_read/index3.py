import pandas as pd
import numpy as np

raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')
# print (raw_data.isna())
# print (raw_data.isna().sum())

# print (raw_data.describe())

# Mencari nilai maksimum dari tiap kolom
# print('Mencari nilai maksimum dari tiap kolom')
# raw_data.max()
 
# # Mencari nilai maksimum dari kolom 'Harga'
# raw_data['Harga'].max()
 
# # Mencari nilai minimum dari kolom 'Harga'
# raw_data['Harga'].min()

# menghitung jumlah dari semua kolom
print ('menghitung jumlah dari semua kolom', raw_data.sum())
 
# menghitung jumlah dari semua kolom bertipe data numerik saja
print('menghitung jumlah dari semua kolom bertipe data numerik saja', raw_data.sum(numeric_only=True))
raw_data.sum(numeric_only=True)
 
# menghitung jumlah dari kolom 'Harga' dan 'Pendapatan'
raw_data[['Harga', 'Pendapatan']].sum()

# Memilih kolom 'Pendapatan' saja
print (raw_data[['Pendapatan']])
 
# Memilih kolom 'Jenis Kelamin' dan 'Pendapatan'
print (raw_data[['Jenis Kelamin', 'Pendapatan']])

# Mengambil data dari baris pertama (indeks 0) hingga baris ke-9 (indeks 9), yaitu sebanyak 10 baris
print(raw_data[:9])
 
# Mengambil data dari baris ke-4 (indeks 3) hingga baris ke-5 (indeks 4)
print(raw_data[3:5])
 
# Mengambil data dari baris ke-2 (indeks 1), baris ke-4 (indeks 3), dan baris ke-11 (indeks 10)
print(raw_data.loc[[1,3,10]])

# Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dari baris ke-2 (indeks 1) hingga baris ke-10 (indeks 9)
print(raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])
 
# Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dari baris ke-2 (indeks 1), baris ke-11 (indeks 10), dan baris ke-16 (indeks 15)
print(raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1,10,15]])

# mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print(produk_A['Pendapatan'].mean())
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print(np.mean(produk_A['Pendapatan']))