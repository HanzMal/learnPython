import requests
url = "https://dqlabcdn.xeratic.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print("isi response",response)
# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
	print(baris)

print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text)