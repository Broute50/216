
# -*- coding: utf-8 -*-
import random
liste = ['1','2','3','4','5','6','7','8','9']
liste1 = ['1','2','3','4','5','6']
liste2 = ['1','2','3','4']

ilksecim = random.choice(liste)
ikincisecim = random.choice(liste1)
ucuncusecim = random.choice(liste2)

print(ilksecim)
print(ikincisecim)
print(ucuncusecim)

sayi1 = str(input(" Lütfen 1' den 9' a kadar lütfen bir rakam giriniz : "))

if sayi1 == ilksecim :
    print(" Tebrikler İkinci Aşama İçin Hak Kazandınız... :)")
    sayi2 = str(input(" Lütfen 1' den 6' ya kadar bir rakam giriniz : "))
    
    if sayi2 == ikincisecim :
        print(" Tebrikler Üçüncü Aşama İçin Hak Kazandınız... :)")
        sayi3 = str(input(" Lütfen 1' den 4' e kadar bir rakam giriniz : "))
        
        if sayi3 == ucuncusecim :
            print(" Tebrikler Yarışmayı Kazandınız!!! ")
        else :
            print(" Üzgünüz Elendiniz :((( ")
    else :
        print(" Üzgünüz Elendiniz :((( ")
else :
    print(" Üzgünüz Elendiniz :((( ")
            