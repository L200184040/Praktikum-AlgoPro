#Activity 1
h=('b','N','a','A','K','p','f')
p={'b':'''Pilihan yang tersedia:
b menampilkan bantuan ini
N menampilkan NIM
a menampilkan Nama
A menampilkan Alamat
K menampilkan Kode Pos
p menampilkan Program Studi
f menampilkan Fakultas''',
   'N':'NIM: L200184040',
   'a':'Nama: Aqshal Fatwa Ibrahim',
   'A':'Alamat: Gemolong Rt002/002, Gemolong, Sragen',
   'K':'Kode Pos: 57274',
   'p':'Program Studi: Informatika (kelas internasional)',
   'f':'Fakultas: Komunikasi dan Informatika (FKI)'}
x=input('Masukkan pilihan anda: ')
if x in h:
    print(p[x])
else:
    print('Pilihan tidak dikenal')