# - Kullanıcıdan alacağınız 5 tane sayının asal olup olmadığını kontrol edip, her bir sayı için
#ekrana sayı asalsa asal, asal değilse asal değil yazdırın.
x=0
while x<5:
    sayi=int(input("Bir sayı gırınız:"))
    if (sayi%2 == 0):
        print("Bu sayı asal değildir.")
    else:
        print("Bu sayı asaldır.")
    
    x +=1
