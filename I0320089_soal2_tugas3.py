
# Nama, Hobi, Sosial media, Lagu kesukaan, Makanan favorit
dict = {'Nama': 'Saida', 'Hobi1': 'Membaca', 'Hobi2': 'Menyanyi', 'Hobi3': 'Tidur', 'Sosmed1': 'Ig: @Rahmaafifi_', 'Sosmed2': 'Twitter: @raraggh_', 'Sosmed3': 'linkedIn: Saida Rahma', 'Lagu1': 'Blue jeans', 'Lagu2': 'yesterday', 'Lagu3': 'i belong to you', 'Makanan1': 'nasi goreng', 'Makanan2': 'martabak', 'Makanan3': 'indomie'}
print("dict:", dict)

# Mengubah Hobi dan Sosial media
dict['Hobi1'] = 'main'
dict['Sosmed1'] = 'LINE: @Rahmafifiy'
print("dict setelah salah satu hodi dan sosial media diubah:", dict)

# Menghapus 2 makanan favorit
del dict['Makanan1']
del dict['Makanan3']
print("dict setelah 2 makanan favorit dihapus:", dict)

# Menambah 1 hobi baru
dict['Hobi4'] = 'jalan jalan'
print("dict setelah menambah hobi baru:", dict)



