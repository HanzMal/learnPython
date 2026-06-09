# string manipulation contoh
nama_produk = "Sepatu Niko"
nama_produk = nama_produk[:2] + "P" + nama_produk[3:9] + "K" + nama_produk[-1] 
print(nama_produk)
print(nama_produk[:7])
print(nama_produk[7:])
print(len(nama_produk))

# string manipulation contoh 2
nama_depan = 'John'
nama_belakang = 'Doe'
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap)
umur = '27 tahun'
alamat = 'Jl. Anggrek No. 100'
nama_umur_alamat = 'Hi, saya ' + nama_lengkap + ' umur ' + umur + ', tinggal di ' + alamat + '.'
print(nama_umur_alamat)

# string manipulation menghilangkan spasi
# Fitur .strip()
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Fitur .lstrip()
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Fitur .rstrip()
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)

# string manipulation kapital
# Fitur .capitalize()
print(">>> Fitur .capitalize()")
judul_buku = 'belajar bahasa Python'
print(judul_buku.capitalize())
# Fitur .lower()
print(">>> Fitur .lower()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.lower())
# Fitur .upper()
print(">>> Fitur .upper()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.upper())