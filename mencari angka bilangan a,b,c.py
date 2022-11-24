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