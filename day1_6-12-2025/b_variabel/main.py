from typing import Final # library buat nilai konstan

"""Mengacu ke dokumentasi PEP 8 – Style Guide for Python Code, 
nama variabel dianjurkan untuk ditulis menggunakan snake_case."""

nama_depan = "Ian"
nama_belakang = "Rush"

# Tipe data bisa ditulis secara eksplisit
umur: int = 18

""" Dalam python juga ada nilai konstanta = 
Konstanta (atau nilai konstan) adalah sebuah variabel yang nilainya dideklarasikan di awal 
dan tidak bisa diubah setelahnya."""

PI: Final = 3.14
print("pi: %f" % (PI))