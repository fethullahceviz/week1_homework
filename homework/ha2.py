kullaniciAdi = input("Kullanici adi giriniz :").upper()
kullaniciSoyadi = input("Kullanici soyadi giriniz :").upper()
ogrenciNo = int(input("Ogrenci numaranizi giriniz :"))
print(f"Adi Soyadi: {kullaniciAdi} {kullaniciSoyadi}",
      f"Ogrenci No: {ogrenciNo}", sep="\n")
print("==========================")

for i in range(4):
    ders = input("Ders adi:").upper()
    # not
    vize = input("Vize notunuzu giriniz :")
    final = input("Final notunuzu giriniz :")

    ort = float(int(vize) * 0.40 + int(final) * 0.6)

    if ort >= 50:
        print( f"Ders Adi: {ders:<12}" , f"Ortalamaniz: {ort:^5}","GECTINIZ")
      
    else:
        print(f"Ders Adi: {ders:<12}", f"Ortalamaniz: {ort:^5}","KALDINIZ")