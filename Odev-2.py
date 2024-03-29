from odev2 import *
def main():
    metin = input("Lütfen metni girin: ")
    frekanslar = harf_frekansi(metin)
    
    print("Karakter Frekansları:")
    for karakter, frekans in sorted(frekanslar.items()):
        print(f"{karakter}: {frekans}   %{frekans:.2f}")

    print(benim_bilgilerim())

if __name__ == "__main__":
    main()
