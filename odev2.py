def is_harf(karakter):
    return karakter.isalpha()


def kucuk_harf(karakter):
    return karakter.lower()


def harf_frekansi(metin):
    frekanslar = {}
    toplam_karakter_sayisi = 0

    for karakter in metin:
        if is_harf(karakter):
            karakter = kucuk_harf(karakter)
            frekanslar[karakter] = frekanslar.get(karakter, 0) + 1
            toplam_karakter_sayisi += 1


    return {harf: frekans / toplam_karakter_sayisi * 100 for harf, frekans in frekanslar.items()}

def benim_bilgilerim():
    return "Merhaba ben adım Elife. Konya teknik üniversitesi bilgisayar mühendisliği 4. sınıf öğrencisiyim. Bir kedi annesiyim. Haydut adında 5 yaşında bir kedim var."