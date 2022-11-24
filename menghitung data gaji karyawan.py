gaji = int(input('masukan gaji: '))
Berkeluarga = (False, True)[input("Sudah berkeluarga?(Y/T)")== "Y"]
Punya_rumah = (False, True)[input("Punya rumah?(Y/T)")== "Y"]
asuransi = (False, True)[input("wajib asuransi dan menabung untuk pensiun? (Y/T)") == "Y"]
pajak = (False, True)[input("wajib bayar pajak atau tidak wajib pajak? (Y/T)") == "Y"]
if gaji > 3000000:
    print ('gaji sudah diatas umr')
    if berkeluarga :
        print ('wajib ikutan asuransi dan menabung untuk pensiun')
    else:
        print ('tidak perlu ikatan asuransi')
    if punya_rumah :
        print ('wajib bayar pajak rumah')
    else:
         print ('tidak wajib bayar pajak rumah')
else:
    print ('gaji belum umr')