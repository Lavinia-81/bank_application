

def function(a: int, b):
    try:
        a = int(a)
        b = int(b)
        response = int(a) / int(b)
    # except ValueError as e:
    #     response = a + b
    # except TypeError as e:
    #     response = a + b
    except ValueError as e:
        try:
             print("Nu pote fi executa impartirea, incerc cancatenare")
             response = a + b
        except Exception as e:
             response = "Nu se fac operatii pe cei doi parametri"
    except TypeError as e:
          try:
              print("Nu pot executa impartirea, incerc cancatenare")
              response = a + b
          except Exception as e:
              response = "Nu se fac operatii pe cei doi parametri"
    finally:
        return response


while True:
    x = input("Prima varianta: ")
    y = input("A doua varianta: ")

    print(function(x, y))
