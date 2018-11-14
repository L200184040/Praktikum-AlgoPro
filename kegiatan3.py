Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama='Aqshal Fatwa Ibrahim'
>>> NIM='L200184040'
>>> X='1'+NIM[7:]
>>> a=int(X)
>>> b=len(Nama)
>>> type(a)
<class 'int'>
>>> #This command is used to find the class (data type) of variable "a". And the data type of variable "a" is int (Integer)
>>> type(b)
<class 'int'>
>>> #This command is used to find the class (data type) of variable "b". And the data type of variable "b" is int (Integer)
>>> a/b
52.0
>>> #This command is used to divide the variable "a" by the variable "b". And the result is in float, it is 52.0
>>> a//b
52
>>> #This command is used to divide the variable "a" by the variable "b". And the result is in integer, it is 52
>>> 10*(a-99)
9410
>>> #This command is used to find the result of mathematic operation. The variable "a" is minus by 99, and then multiplied by ten. And the result is 9410.
>>> b**2
400
>>> #This command is used to find the result of variable "b" powered by two. And the result is 400
>>> a%b
0
>>> #This command is used to find the rest of divider from the division of variable "a" by variable "b". And the result is 0
>>> c=12.5
>>> #This command is used to give value of the variable "c" by 12.5
>>> type(c)
<class 'float'>
>>> #This command is used to find the data type of the variable "c". And the data type of variable "c" is float (real number).
>>> a/c
83.2
>>> #This command is used to divide the variable "a" by the variable "c". And the result is in float, it is 83.2
>>> a//c
83.0
>>> #This command is used to divide the variable "a" by the variable "c". And the result is in float, it is 83.0
>>> a%c
2.5
>>> #This command is used to find the rest of divider from the division of variable "a" by variable "c". And the result is 2.5
>>> c>b
False
>>> #This command is used to check the result if the operation is true or false. The result from variable "c" is bigger than variable "b" is False.
>>> type(c>b)
<class 'bool'>
>>> #This command is used to find the data type of operation "variable c is bigger than variable b". And the data type is bool (Boolean).
>>> a>b and b>c
True
>>> #This command is used to check the result of the operation "variable a is bigger than variable b" and the operation "variable b is bigger than variable c". And the result is True.
>>> a>1100 or b<10
False
>>> #This command is used to check the result of the operation "variable a is bigger than 1100" and the operation "variable b is smaller than 10". And the result is False.
>>> 
