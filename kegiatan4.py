Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama='Aqshal Fatwa Ibrahim'
>>> NIM=1040
>>> Tinggi=187
>>> Berat=55
>>> TahunLahir=2000
>>> Aku=(TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data=[TahunLahir,Berat,Tinggi,NIM,Nama]
>>> type(Aku)
<class 'tuple'>
>>> #This command is used to find the class (data type) of variable "Aku". And the data type of variable "Aku" is Tuple. Tuple is a group of data that is non-mutable, can't be edited.
>>> Aku[0]
2000
>>> #This command is used to return value of the first data of "Aku" Tuple.
>>> a=NIM%4;Aku[a]
2000
>>> #The value of NIM%4 is 0. The command 'Aku[a]' is to looking for a data in the Aku variable with index a. a equal 0. And the data in the Aku variable with index 0 is 2000 (TahunLahir)
>>> type(Aku[a])
<class 'int'>
>>> #This command is used to find the data type of variable "Aku[a]". The data type of "Aku[a]" variable is int (Integer)
>>> Aku[a:4]
(2000, 55, 187, 1040)
>>> #This command is used to slice the tuple "Aku" from "a" index until 4th index. The value of "a" variable is 0. So, it will slice data from the index 0 until index 4.
>>> type(Aku[4])
<class 'str'>
>>> #This command is used to find the data type of variable "Aku[4]". The data type of "Aku[4]" variable is str (String)
>>> Aku[0]='ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0]='ok'
TypeError: 'tuple' object does not support item assignment
>>> #Python gives error message, because "Aku" is a Tuple, so it is non-mutable, can't be edited.
>>> type(Data)
<class 'list'>
>>> #This command is used to find the data type of variable "Data". And the data type of variable "Data" is List. List is a group data that is mutable, it is can be edited.
>>> type(Data[4])
<class 'str'>
>>> #This command is used to find the data type of variable "Data[4]". The data type of "Data[4]" variable is String.
>>> Data[4][5]
'l'
>>> #The 4th index of "Data" list is "Nama" variable, the command used to return the 5th index's value of the "Nama" variable. Then the value is "l"
>>> Data[4][a:6]
'Aqshal'
>>> #The 4th index of "Data" list is "Nama" variable, index of "a" is 0. This command used to slice the "Nama" variable from the index 0 until 6th index.
>>> Data[0]='ok';Data
['ok', 55, 187, 1040, 'Aqshal Fatwa Ibrahim']
>>> #This command is used to change the 0 index of "Data" list with the 'ok' value. Then, the command will return the list of "Data"
>>> Data[-a]
'ok'
>>> #This command is used to return the -a index (-0) of the "Data" list
>>> range(a)
range(0, 0)
>>> #This command is used to make range at range a (0).
>>> 
