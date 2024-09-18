import random
# İSİM  GİRME 
#print(input(" adinizi giriniz  : "))

# --- ortalama hesaplama ---
#s1 = float(input(" ilk sayiyi girin  : "))
#s2 = float(input(" ikinci sayiyi giriniz  : "))
#print(s1 + s2)
#print("ortalama")
#print((s1 + s2)/2)

# --- VİZE HESAPLAMA ---  
#vize = float(input(" vize notunu giriniz : "))
#final = float(input(" final notunu giriniz  : "))
#print((vize + final)/2)

# --- 3 NOT ORTALAMA ---
#n1 = float(input(" ilk notu girin  : "))
#n2 = float(input(" ikinci notu giriniz  : "))
#n3 = float(input(" üçüncü notu giriniz  : "))
#print((n1 + n2 + n3)/3)


# --- GEÇME KALMA İF ELSE ---
#n1 = float(input(" notu ortalamasını girin  : "))
#if(n1 < 50 ):
#    print("Kaldı")
#else:
#    print("Geçti")

# --- 22.ÖRNEK ---
"""çiftsayilar = 0
teksayilar = 0
sayi = int(input("Sayıyı girin : "))
for i in range(sayi):
    if (i%2==0):
        çiftsayilar+=i

    elif(i%2==1):
        teksayilar+=i
print("çift sayıların toplamı = " , çiftsayilar)
print("tek sayıların toplamı = " , teksayilar)"""

# ASAL SAYI ÖRNEK
"""for asa in range (2,a):
     if(a%asa==0):
          print("asal değil")
          break
     else: 
        print("asal")
        break"""

# --- MAAŞA ZAM ÖRNEĞİ ---
"""maas = float(input(" Maaşınızı girin  : "))
zam = float(input(" Zam oranını girin (%)  : "))
yenimaas = maas + (maas * zam/100)
print("yeni maaşınız = ",yenimaas)"""


# --- FONKSİYON ÖRNEK ---
"""def fonksiyon():
    kisak = int(input(" Kısa kenarı giriniz : "))
    uzuk = int(input(" Uzun kenarı giriniz : "))    
    print(kisak*uzuk)

fonksiyon()

def dairealan():
    r = int(input(" Yarıçapı giriniz : "))
    alan = 3*r**2
    print(alan)
dairealan()"""

# --- SAYI TAHMİN OYUNU ---
"""hak = 3
c = random.randint(1,100)
print(c)
while hak > 0:
    t = int(input("Tahmin girin : "))
    if(t == c):
        print("Tebrikler Kazandınız ")
        break
    elif(t < c):
        print("Daha büyük bir sayı girin")
        hak-=1
    elif(t > c):
        print("Daha küçük bir sayı girin")
        hak-=1

if(hak == 0):
    print("Kaybettiniz")"""

# DATETİME 
"""from datetime import datetime


tarih_str = input("Tarihi gir ")



tarih = datetime.strptime(tarih_str, "%d-%m-%Y")
    
gun_numarasi = tarih.timetuple().tm_yday
print(f"{tarih_str} tarihi yılın {gun_numarasi}. günü.")"""

# ÇİFT ORTALAMA ALMA

"""def cift_mi(sayi):
    
    return sayi % 2 == 0


sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = 0
sayi_adedi = 0


for sayi in range(sayi1,sayi2):
    if cift_mi(sayi):
        toplam += sayi
        sayi_adedi += 1



ortalama = toplam / sayi_adedi
print(ortalama)"""


# DİKDÖRTGEN ALAN
"""def dikdortgen_alani(genislik, yukseklik):
    
    return genislik * yukseklik


genislik = int(input("genişliğini "))
yukseklik = int(input(" yüksekliğini "))


alan = dikdortgen_alani(genislik, yukseklik)"""

# GÜN HESAPLAMA

"""gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

indeks = int(input("0-4 arası sayı gir"))


print(f"Girilen indeksteki gün: {gunler[indeks]}")"""

# --- KARAKTER BULMA ---
"""def karakter_var_mi(metin, karakter):

    if karakter in metin:
        return True 
    else:
        return False 
metin = "Merhaba, dünya!" 
karakter = "d"  
if karakter_var_mi(metin, karakter):
    print(f"'{karakter}' karakteri metin içinde bulunmaktadır.")
else:
    print(f"'{karakter}' karakteri metin içinde bulunmamaktadır.")"""

"""# --- KULLANICININ GİRDİĞİ SAYILARI TOPLAMA ---
sayi = str(input("sayı giriniz : "))
toplam = 0
for i in sayi:
    toplam += int(i) 
print(toplam)"""

# 0 BASILANA KADAR TOPLAMA

"""toplam = 0


while True:
    sayi = float(input(" sayı gir "))
    
    if sayi == 0:
        break  
    
    toplam += sayi 


print(toplam)"""

"""# 5 İN KATLARINI LİSTELEME
listea=[1,4,5,10,14,20]
listeb =[]
for i in listea:
    if (i%5==0):
        listeb.append(i)
print(listeb)"""

"""# 10 20 ARASI SAYILARDAN LİSTE YAPMA
sayilar = [10,11,12,13,14,15,16,17,18,19,20]
sayilar2 = [21,22,23,24,25]
sayilar.extend(sayilar2)
for i in sayilar:
    if (i%4==0):
        print(i)"""
    
# --- TEK ÇİFT POZİTİF NEGATİF ---
"""sayi = int(input("Sayı girin"))
if (sayi%2==0):
    print("Sayı çift ")
else:
    print("sayı tek")
if(sayi <0):
    print("sayı negatif")
elif(sayi==0):
    print("sayı 0 ")
else:
    print("sayı pozitif")"""



# --- VKİ HESAPLAMA ---
"""boy=int(input("boyunuzu girin (m) "))
kilo=int(input("boyunuzu girin"))
vki = kilo/(boy*boy)
if (vki < 18):
    print(" Zayıf ")
elif (vki > 25):
    print(" Kilolu ")
else:
    print("Normal")"""

# --- FOR ÖRNEK ---
"""for i in range(100):
    print(i+1)
    
for i in range(100):
    if(i%2==0):
        print(i)

for i in range(100):
    if(i%2==1):
        print(i)        
for i in range(100):
    if(i%5==0 & i%3==0):
        print(i)"""

# --- Liste Örnek ---
"""sayi = int(input(" sayı girin : "))
liste = []
for i in range(sayi):
    liste.append(i)"""


"""metin = str(input("metin girin : "))
for karakter in (metin):
    print(karakter)"""