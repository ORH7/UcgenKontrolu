kenar1 = int(input("Üçgenin 1.Kenarını giriniz: "))
kenar2 = int(input("Üçgenin 1.Kenarını giriniz: "))
kenar3 = int(input("Üçgenin 1.Kenarını giriniz: "))

# kenarları sıralayan if else yapısı
if kenar1 > kenar2 :
    if kenar1 > kenar3:
        uzun_kenar = kenar1
        kisa_kenar = kenar2
        orta_kenar = kenar3
    else:
        uzun_kenar = kenar3
        kisa_kenar = kenar2
        orta_kenar = kenar1
else:
    if kenar3 > kenar2:
        uzun_kenar = kenar3
        kisa_kenar = kenar1
        orta_kenar = kenar2

    else:
        uzun_kenar = kenar2
        kisa_kenar = kenar1
        orta_kenar = kenar3

# Üçgen olup olmadığını kontrol eden if yapısı
if kenar1 > kenar2+kenar3 or kenar2>kenar3+kenar1 or kenar3> kenar2+kenar1:
    print("Üçgen değil")
else:
    uzun_kenar_kare= uzun_kenar**2
    kisa_kenarlarin_kareler_toplami=kisa_kenar**2+orta_kenar**2

    # Üçgen çeşitlerini belirleyen if else yapısı
    if kenar1 == kenar2== kenar3:
        print("Eşkenar Üçgen")
    elif uzun_kenar_kare==kisa_kenarlarin_kareler_toplami:
        print("Dik üçgen")
    elif uzun_kenar_kare > kisa_kenarlarin_kareler_toplami:
        print("Geniş Üçgen")
    else:
        print("Dar Üçgen")