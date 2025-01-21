counter = 0
while counter<3:
    try:
        a = int(input("Citeste primul numar: "))
        b = int(input("Citeste al doilea numar: "))
        if b > 10000:
            raise Exception("Numarul cu care se imparte este prea mare")
        # f = open("cba.txt", "r")
        print(f"Raspunsul este {a / b}")
    except ZeroDivisionError as e:
        print(f"Except este {e}")
        print("Infinit")
    except ValueError as e:
        print(f"Exceptia este {e}")
        print("Nu se accepta decat numere intregi")
        break
    except Exception as e:
        print(f"Exceptie neprevazuta!!! {e}")
    else:
        print("Ruleaza numai cand se executa cu succes try-ul")
    finally:
        print("Se executa orice ar fi!!!")

else:
    print("Am iesit")