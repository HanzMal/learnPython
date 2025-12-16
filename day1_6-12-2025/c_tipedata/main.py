# Beragam tipe data di python

# 1. String
# string sebaris
string_1 = "hello python"

# string multi-baris
string_2 = """Selamat
Belajar
Python"""

# 2. Bool true | false
bool_1 = True
bool_2 = False

# 3. Tipe data None merepresentasikan nilai kosong (seperti nilai null atau nil di bahasa lain).
data = None
print(data)

# 4. List adalah tipe data di Python untuk menampung nilai kolektif yang disimpan secara urut, dengan isi bisa berupa banyak varian tipe data (tidak harus sejenis). Cara penerapan list adalah dengan menuliskan nilai kolektif dengan pembatas , dan diapit tanda [ dan ].
# Mirip array

# list with str as element's data type
list_2 = ["grayson", "jason", "tim", "damian"]

# list with various data type in the element
list_3 = [24, False, "Hello Python"]
print(list_3[2]) # akses data indeks ke 2

# 5. Tuple = mirip list yang merupakan nilai kolektif. namun menggunakan tanda kurung () dan tidak mutable
# tuple with int as element's data type
tuple_1 = (2, 3, 4)
print(tuple_1[0])

# 6. Tipe data dict atau dictionary berguna untuk menyimpan data kolektif terstruktur berbentuk key value. 
player_1 = {
  "name": "Ronaldo",
  "is_male": True,
  "age": 40,
  "skills": ["heading", "shooting"]
}
print("skills: %s" % (player_1["skills"]))
