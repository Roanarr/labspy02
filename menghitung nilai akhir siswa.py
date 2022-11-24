nama = int(input('masukan nama: '))
uts = int(input('masukan nilai UTS: '))
uas = int(input('masukan nilai UAS: '))
tugas = int(input('masukan nilai Tugas: '))
akhir = (int(tugas)*.2)+(int(uts)*.4)+(int(uas)*.4)
keterangan = ('TIDAK LULUS',"LULUS")[akhir > 60.0]

if akhir > 80:
    huruf = 'a'
elif akhir > 70:
    huruf = 'b'
elif akhir > 50:
    huruf = 'c'
elif akhir > 40:
    huruf = 'd'
else:
    huruf = 'e'

print('\nNama :',nama)
print('nilai uts :',uts)
print('nilai uas :',uas)
print('nilai tugas :',tugas)
print('nilai akhir :',akhir)
print('\nNilai huruf :',huruf)
print('keterangan :',keterangan)