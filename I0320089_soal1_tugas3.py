#membuat list teman
list_teman = ['vincent','sekar','sasa','salma','yuku','ryan','alvin','william','tito','titus']

#menampilkan isi indeks nomor 4,6,7
print("nama teman 4,6,7 : ",list_teman[3], ",", list_teman[5], ",", list_teman[6])

#mengganti nama teman di list 3,5,9
list_teman [2] = 'maurich'
list_teman [4] = 'tsania'
list_teman [8] = 'zafira'

#menanbah 2 nama teman
list_teman.append('sony')
list_teman.append('yola')

#menampilkan list nama teman dengan pengulangan
print(list_teman*4)

#menampilkan panjang list
print(len(list_teman))