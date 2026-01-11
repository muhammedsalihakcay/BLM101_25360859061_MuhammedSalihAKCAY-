def rle_encode(metin):
    """
    Bu fonksiyon kullanıcıdan alınan metni
    Run-Length Encoding  yöntemi ile sıkıştırma yapar

    """

    # eğer metin boşsa boş string döndürmeye yarar
    if not metin:
        return ""

    encoded_metin = ""   # Sıkıştırılmış metni tutar
    sayı = 1           # Ardışık tekrar sayısını tutar


    for i in range(1, len(metin)):               # Metnin ikinci karakterinden başlayarak kontrol edilir

        if metin[i] == metin[i - 1]:            # Eğer karakterler aynıysa tekrar sayısını artır
            sayı += 1
        else:

            encoded_metin += str(sayı) + metin[i - 1]               # farklı karakter gelince önceki karakter ve sayısı yanına eklenir
            sayı = 1                                            # sayaç sıfırlanır


    encoded_metin += str(sayı) + metin[-1]           # Son karakter grubu eklenir

    return encoded_metin


def rle_decode(encoded_metin):
    """
    Bu fonksiyon rle ile sıkıştırılmış metni
    tekrar orijinal haline çevirir.
    """

    decoded_metin = ""        # Açılmış metni tutar
    sayı = ""               # Sayıları geçici olarak tutar

    for char in encoded_metin:

        if char.isdigit():               # eğer karakter sayıysa tekrar sayısına eklenir
            sayı += char
        else:

            decoded_metin += char * int(sayı)           # harf geldiğinde harfi count kadar ekler
            sayı = ""        # sayaç sıfırlanır

    return decoded_metin


def sıkıstırma_oran(orijinal, encoded):
    """
    Bu fonksiyon orijinal metin ile sıkıştırılmış metin
    arasındaki sıkıştırma oranını yüzdesini hesaplar
    """

    orijinal_boyut = len(orijinal)  # orijinal metnin uzunluğu
    encoded_boyut = len(encoded)    # sıkıştırılmış metnin uzunluğu

    oran = (1 - (encoded_boyut / orijinal_boyut)) * 100
    return oran


# ---------------- ANA PROGRAM ----------------

# Kullanıcıdan metin alınır
orijinal_metin = input("Sıkıştırılacak metni giriniz: ")

# RLE sıkıştırma işlemi
encoded_metin = rle_encode(orijinal_metin)

# RLE  decode  işlemi
decoded_metin = rle_decode(encoded_metin)

# Sıkıştırma oranı
oran = sıkıstırma_oran(orijinal_metin, encoded_metin)

# Sonuçlar ekrana yazdırılır
print("\n--- RLE SONUÇLARI ---")
print("Orijinal Metin      :", orijinal_metin)
print("Sıkıştırılmış Metin :", encoded_metin)
print("Açılmış Metin       :", decoded_metin)
print("Sıkıştırma Oranı    : %.2f%%" % oran)
