urunler = []
fiyatlar = []

while True:
    print("\n--- SEPET UYGULAMASI ---")
    print("1- Ürün ekle")
    print("2- Sepeti listele")
    print("3- Toplam tutarı göster")
    print("4- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        urun = input("Ürün adı: ")
        fiyat = float(input("Ürün fiyatı: "))

        urunler.append(urun)
        fiyatlar.append(fiyat)

        print("Ürün sepete eklendi.")

    elif secim == "2":
        if len(urunler) == 0:
            print("Sepet boş.")
        else:
            print("\nSepetteki ürünler:")
            for i in range(len(urunler)):
                print(urunler[i], "-", fiyatlar[i], "TL")

    elif secim == "3":
        toplam = 0
        for fiyat in fiyatlar:
            toplam += fiyat

        print("Toplam tutar:", toplam, "TL")

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")
