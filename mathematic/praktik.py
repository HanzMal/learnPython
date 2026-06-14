import requests
from contextlib import closing
import csv
# STEP 1: 
# Baca file "harga_rumah.txt"
url = "https://dqlabcdn.xeratic.com/dqlab-dataset/harga_rumah.txt"
data_harga_rumah = []
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    data_harga_rumah = [row for row in csv.reader(f)]

print(data_harga_rumah)