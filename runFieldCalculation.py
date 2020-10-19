def wybierz(q):
    print("============================================================")
    print(q, " Wybierz numer figury której pole chcesz obliczyć.")
    print("============================================================")

    print("""
                  +------------+
                  |1. Prostokąt| 
                  |2. Kwadrat  |
                  |3. Trójkąt  |
                  |4. Trapez   |
                  |5. Koło     |
                  +------------+
              """)

    print("       ====================================")
    print("       Jeśli chcesz zakończyć wpisz numer 6")
    print("       ==================================== \n")

def wybor(t):
    print("==========================")
    print("Wybrałeś pole", t)
    print("==========================")
    print("\n")

def nie():
    print("Żadna długość nie może być mniejsza od 1!")

i = 1



wybierz("Witaj!")

while i != 0:

    numer = input("Tutaj podaj numer który wybierasz --> ")
    print("\n")


    if(numer == "1"):

        wybor("prostokąta!")

        a = int(input("Wprowadz długość pierwszego boku: "))
        if(a >= 1):
            b = int(input("Wprowadz długość drugiego boku: "))
            if(b >=1):
                print()
            else:
                nie()    
        elif(a <= 0):
            nie()

        print("---> Pole wynosi: ", a*b, "<--- \n") 



    elif(numer == "2"):
        
        wybor("kwadratu!")

        a=int(input("Wprowadź długość boku: "))
        if(a >=1):
            print("---> Pole wynosi: ", a*a, "<--- \n")
        else:
            nie()



    elif(numer == "3"):
        
        wybor("trójkątu!")

        a = int(input("Wprowadź długość podstawy: "))
        if(a >= 1):
            h = int(input("Podaj wysokość: "))
            if(h >= 1):
                print()
            else:
                nie()
        else:
            nie()

        print("---> Pole wynosi: ", 0.5*a*h, "<--- \n")
            


    elif(numer == "4"):

        wybor("trapezu!")

        a = int(input("Wprowadz długość pierwszego boku: "))
        if(a >= 1):
            b = int(input("Wprowadz długość drugiego boku: "))
            if(b >=1 and a != b):
                 h = int(input("Podaj wysokość: "))
                 if(h <= 0):
                     nie()
                 else:
                     print()
            elif(b == a):
                     print("Boki równoległe nie mogą być takiej samej długości \n")       
            else:
                nie()    
        elif(a <= 0):
            nie()
        if(a != b):
            w = a + b
            w = w * h
            w = w / 2
            
            print("---> Pole wynosi: ", w, "<--- \n")
       
            


        
    elif(numer == "5"):

        wybor("koła!")

        r=int(input("Wprowadź długość promienia: "))
        if(a >=1):
            r = r**2
            print("---> Pole wynosi: ", r*3.14, "<--- \n")
        else:
            nie()


    elif(numer == "6"):
        print("""
                +-------------------------+
                |Czy napewno chcesz wyjść?|
                |                         |
                |   TAK             NIE   |
                +-------------------------+
                \n""")

        wyjscie = input("Wpisz TAK lub NIE: ")

        if(wyjscie == "TAK" or "tak"):
              break
        else:
            print()



    else:
        print("Niestety wybrałeś/aś zły numer. Spróbuj jeszcze raz! \n")
              
        

    wybierz("")
