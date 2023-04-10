def calculateExamAvarage(midterm: float, final: float):
    ortalama = (vize*0.4) + (final*0.6)

    if ortalama<=49 :
        print("Harf notunuz FF.")
    elif  50<= ortalama <=59:
        print("Harf notunuz DD.")
    elif  60<= ortalama <=69:
        print("Harf notunuz CC.")
    elif  70 <= ortalama <=79:
        print("Harf notunuz BB.")
    else:
        print("Harf notunuz AA.")

vize =float(input("Lütfen vize notunuzu giriniz: "))
final = float(input("Lütfen final notunuzu giriniz:"))
calculateExamAvarage(midterm=vize,final=final)

