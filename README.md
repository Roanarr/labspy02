![fix 2](https://user-images.githubusercontent.com/118960008/203722933-cb7abfbd-266e-470d-8ec6-c41c78bacc0b.png)
![fix](https://user-images.githubusercontent.com/118960008/203722707-359a9152-789d-4414-854e-0504326abf49.png)
# Tugas pertemuan 9 
## mencari angka bilangan a,b,c

a = int(input('masukan nilai a:'))

b = int(input('masukan nilai b:'))

c = int(input('masukan nilai c:'))

if a > b and a > c:

print('a yang terbesar')

elif b > a and b > c:

print('b yang terbesar')

else:

print('c yang terbesar')

if a < b and a < c:

print('a yang terkecil')

elif b < a and b < c:

print('b yang terkecil')

else:

print('c yang terkecil')

if (b > a > c) or (c > a > b):

print('a adalah nilai tengah')

elif (a > b > c) or (c > b > a):

print('b adalah nilai tengah')

else:

print('c adalah nilai tengah')
