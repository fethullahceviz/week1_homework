#Stein Papier Schere

oyuncu1     = input("Oyuncu1 :").upper()
print(f"Oyuncu1: {oyuncu1}")
print("==================")
oyuncu2     = input("Oyuncu2 :").upper()
print(f"Oyuncu2: {oyuncu2}")
print("==================")

oyuncu1puan = 0
oyuncu2puan = 0

secim = """
[1] Tas,
[2] Kagit,
[3] Makas
"""
for i in range(10):

    secim1 = int(input(secim))
    secim2 = int(input(secim))

    if secim1 == 1 and secim2 == 2:
        oyuncu2puan += 1
    elif secim1 == 1 and secim2 == 3:
        oyuncu1puan += 1
    elif secim1 == 2 and secim2 == 1:
        oyuncu1puan += 1
    elif secim1 == 2 and secim2 == 3:
        oyuncu2puan += 1
    elif secim1 == 3 and secim2 == 1:
        oyuncu1puan += 1
    elif secim1 == 3 and secim2 == 2:
        oyuncu2puan += 1

print(f"{oyuncu1} Puan: {oyuncu1puan}")
print(f"{oyuncu2} Puan: {oyuncu2puan}")
print("==================")

if oyuncu2puan > oyuncu1puan:
    print(f"Kazanan Oyuncu: {oyuncu2}")

elif oyuncu1puan > oyuncu2puan:
    print(f"Kazanan Oyuncu: {oyuncu1}")
else:
    print("Berabere")