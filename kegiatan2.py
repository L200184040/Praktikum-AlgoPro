##Program Akun
##Dibuat oleh Aqshal Fatwa Ibrahim
Nama='Aqshal Fatwa Ibrahim'
TanggalLahir='18 April 2000'
print('Nama singkat =',Nama[:6],Nama[7]+'.',Nama[-7]+'.')
print('Username =',Nama[0]+TanggalLahir[:2]+TanggalLahir[-4:])

import random
print('Password =',Nama[:3]+str(random.randint(0,1000)))