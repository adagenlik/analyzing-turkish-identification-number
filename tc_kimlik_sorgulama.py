tc=input("Tc Kimlik Numaranızı Giriniz:")
tc1=int(tc[0])
tc2=int(tc[1])
tc3=int(tc[2])
tc4=int(tc[3])
tc5=int(tc[4])
tc6=int(tc[5])
tc7=int(tc[6])
tc8=int(tc[7])
tc9=int(tc[8])
tc10=int(tc[9])
tc11=int(tc[10])

madde3=(((tc1+tc3+tc5+tc7+tc9)*7)-(tc2+tc4+tc6+tc8))%10
madde4=(tc1+tc2+tc3+tc4+tc5+tc6+tc7+tc8+tc9+tc10)%10

if(len(tc) == 11):
    print("T.C: 11 Haneli")
    if(tc1 != 0):
        print("İlk Basamak 0 Değil")
        if(madde3 == tc10):
            print("3. Doğrulama Doğru")
            if(madde4 == tc11):
                print("4. Doğrulama Doğru")
                print("T.C. Kimlik Numaranız Doğru")
            else:
                print("HATA! 4. Doğrulama Yanlış")
        else:
            print("HATA! 3. Doğrulama Yanlış")
    else:
        ("HATA! İlk Basamak 0 Olamaz")
else:
    ("HATA! T.C. 11 Haneli Değil")