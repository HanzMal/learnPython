# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
aksara = Karyawan()
senja = Karyawan()
# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(aksara.__class__.nama_perusahaan)
# Ubah nama_perusahaan menjadi 'DEF'
aksara.__class__.nama_perusahaan = 'DEF'
# Cetak nama_perusahaan objek aksara dan senja
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)

# perbedaan antara class attribute dan instance attribute
# Definisikan class Karyawan
class Employee:
    nama_perusahaan = 'ABC'
    tunjangan_transportasi = 500000
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        if usia > 30:
            self.pendapatan += 1500000
        self.pendapatan_tambahan = 0

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# karyawan_1 = Employee('Budi', 35, 7500000)
# karyawan_2 = Employee('Didi', 30, 8000000)

karyawan_1 = Employee('Budi', 35, 5000000)
karyawan_2 = Employee('Didi', 30, 5000000)
# karyawan_1.__class__.nama_perusahaan = 1000000 eRROR  

total_pengeluaran = karyawan_1.pendapatan + karyawan_2.pendapatan 
print(total_pengeluaran) # Output: 17000000

# Buat object bernama aksara dan senja
aksara = Employee('Aksara', 25, 8500000)
senja = Employee('Senja', 28, 12500000)
# Cetak objek bernama aksara
print(aksara.nama + ', Usia: ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))
# Cetak objek bernama senja
print(senja.nama + ', Usia: ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))

# Soal lain
total_pengeluaran = karyawan_1.__class__.tunjangan_transportasi
total_pengeluaran += karyawan_2. __class__.tunjangan_transportasi
total_pengeluaran += karyawan_1.pendapatan
total_pengeluaran += karyawan_2.pendapatan
print(total_pengeluaran) #11.000.000

# Aksara melaksanakan lembur
aksara.lembur()
# Senja memiliki proyek tambahan
senja.tambahan_proyek(2500000)
# Cetak pendapatan total Aksara dan Senja
print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' +str(senja.total_pendapatan()))

'''Dari potongan kode di atas, atribut nama, usia dan pendapatan merupakan contoh dari instance variabel. Sebagai tambahan, fungsi __init__() di dalam class Employee secara khusus disebut sebagai constructor. Melalui sebuah constructor, aku dapat meng-assign (menginisialisasi) atribut-atribut milik sebuah objek.

Pada bahasa pemrograman Python, setiap fungsi (termasuk constructor) akan menerima dirinya sendiri (self) sebagai parameter pertama dari fungsi. Kemudian, aku dapat menambahkan parameter-parameter lain setelah parameter self sesuai dengan kebutuhan. Seperti pada contoh di atas, saat objek dibuat (diinisialisasi), aku dapat melemparkan nama, usia dan pendapatan melalui syntax, '''