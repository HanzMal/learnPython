# Fitur .split()
print(">>> Fitur .split()")
frasa = "ani dan budi dan wati dan johan"
karakter = frasa.split("dan")
print(karakter)
kata = frasa.split(" ")
print(kata)
# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
frasa = pemisah.join(karakter)
print(frasa)
frasa = " ".join(karakter)
print(frasa)
# Fitur .replace()
print(">>> Fitur .replace()")
frasa = "apel malang apel yang paling segar, apel sehat, apel nikmat"
frasa = frasa.replace('apel', 'jeruk')
print(frasa)

# Menentukan Posisi dan Jumlah Sub-string pada String
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
print(">>> Fitur .find()")
print(teks.find('Apel'))
print(teks.find('malang'))
# Fitur .count()
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count('apel')
print(kemunculan_kata_apel)

# Menentukan String Apakah Diawali/Diakhiri oleh Sub-string
# Fitur .startswith()
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
# Fitur .endswith()
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))