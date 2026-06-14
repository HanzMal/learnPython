# # Menulis ke file hello.txt
# file = open("hello.txt", "w")
# file.write("Sekarang kita belajar menulis dengan menggunakan Python")
# file.write("Menulis konten file dengan mode w (write).")
# file.close()

# # Menulis ke file dengan mode append
# file = open("hello.txt", "a")
# file.writelines([
# "Sekarang kita belajar menulis dengan Python", 
# "Menulis konten file dengan mode a (append)"
# ])
# file.close()

file = open("hello.txt","a")
file.writelines(["Halo\n", "Belajar Python", "Menyenangkan!"])
# file.close()
# file = open("hello.txt","w")
# file.writelines(["Menulis ke dalam file\n"])
# file.writelines(["menggunakan Python"])
file = open("hello.txt","r")
for line in file:
    print(line)