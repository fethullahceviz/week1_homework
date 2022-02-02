
selamlama = "Beden Kitle Indeksi Hesaplama Modulune hosgeldiniz".upper()
print(selamlama)

kilo    = float(input("Kilonuzu giriniz :")) #kg
boy     = float(input("Boyunuzu giriniz :")) #metre
index   = int(kilo/boy**2)

if index < 25:
    print("=========================")
    print(f"Index:{index}", "NORMAL", sep=" ---> ", end=" < ")
    print("\n=========================")
elif 25 <= index <= 30:
    print("===============================")
    print(f"index : {index}", "FAZLA KILOLU",sep=" ---> ", end=" < ")
    print("\n===============================")

elif 30 < index < 40:
    print("=======================")
    print(f"index : {index}", "OBEZ",sep=" ---> ", end=" < ")
    print("\n=======================")
else:
    print("===============================")
    print(f"index : {index}", "AŞIRI SISMAN",sep=" ---> ", end=" < ")
    print("\n===============================")
