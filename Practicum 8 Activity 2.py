#Activity 2
def konversiSuhu():
    x=int(input('Pilih konversi: '))
    if (x==1):
        f=int(input('Masukkan suhu (Celcius): '))
        c=32+9.0/5*f
        print('Hasilnya adalah',c,'derajat Fahrenheit')
    if (x==2):
        a=int(input('Masukkan suhu (Fahrenheit): '))
        b=(a-32)*5.0/9
        print('Hasilnya adalah',b,'derajat Celcius')
print('''Konversi suhu
1. Celcius ke Fahrenheit
2. Fahrenheit ke Celcius''')
konversiSuhu()