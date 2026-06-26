# Inheritance

Inheritance di OOP itu cara bikin class baru yang "nurun" dari class lama.

Class baru otomatis punya semua atribut dan fungsi milik class lama, tapi cuma yang public aja. Yang private nggak ikut diwarisin.

Intinya: class baru bisa pakai ulang kode class lama tanpa nulis ulang, selama bukan yang private.

Melalui konsep inheritance class AnalisData dan IlmuwanData akan memiliki setiap atribut dan fungsi yang dimiliki oleh class Karyawan (Hal ini dikarenakan seluruh atribut dan fungsi dari class Karyawan bersifat public)

Melalui potongan kode di atas, aku telah menerapkan konsep inheritance. Melalui konsep inheritance class AnalisData dan IlmuwanData akan memiliki setiap atribut dan fungsi yang dimiliki oleh class Karyawan (Hal ini dikarenakan seluruh atribut dan fungsi dari class Karyawan bersifat public)

Pada konsep inheritance, class AnalisData dan class IlmuwanData disebut sebagai child class dari class Karyawan; sehingga class Karyawan dapat disebut sebagai parent class dari class AnalisData dan IlmuwanData

Suatu child class dapat mengakses atribut ataupun fungsi yang dimiliki oleh parent class dengan menggunakan fungsi super(). Pada contoh di atas, fungsi super() digunakan oleh child class (AnalisData dan IlmuwanData) untuk mengakses constructor yang dimiliki oleh parent class (Karyawan)

Metode overloading mengizinkan sebuah class untuk memiliki sekumpulan fungsi dengan nama yang sama dan parameter yang berbeda. Berkaitan dengan hal ini, Python tidak mengizinkan pendeklarasian fungsi (baik pada class ataupun tidak) dengan nama yang sama.

Untuk mengimplementasikan method overloading pada Python, aku dapat menggunakan sebuah teknik yang dikenal dengan function default parameters.
