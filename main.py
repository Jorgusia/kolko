# tu będzie gra kółko i krzyzyk

Plansza_Do_Gry = {'7':' ', '8':' ','9': ' ','4':' ', '5':' ','6': ' ','1':' ', '2':' ','3': ' '}
Klawisze_gry = []

for key in Plansza_Do_Gry:
    Klawisze_gry.append(key)

def drukuj_plansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print("-+-+-")
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print("-+-+-")
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

drukuj_plansze(Plansza_Do_Gry)

def gra():

        gracz = 'X'
        licznik = 0

        for i in range(10):
            drukuj_plansze(Plansza_Do_Gry)
            

            move = input(f'To jest ruch, {gracz}. Wybierz gdzie chcesz postawić znak!')

            if Plansza_Do_Gry[move]==' ':
                Plansza_Do_Gry[move] = gracz
                licznik += 1
            else:
                print('Miejsce jest ju zajętę. \nWybierz inne miejsce!')
                continue

            if licznik >= 5:
                if Plansza_Do_Gry['7'] == Plansza_Do_Gry['8'] == Plansza_Do_Gry['9'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['4'] == Plansza_Do_Gry['5'] == Plansza_Do_Gry['6'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['1'] == Plansza_Do_Gry['2'] == Plansza_Do_Gry['3'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['1'] == Plansza_Do_Gry['4'] == Plansza_Do_Gry['7'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['2'] == Plansza_Do_Gry['5'] == Plansza_Do_Gry['8'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['3'] == Plansza_Do_Gry['6'] == Plansza_Do_Gry['9'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['1'] == Plansza_Do_Gry['5'] == Plansza_Do_Gry['9'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break
                elif Plansza_Do_Gry['3'] == Plansza_Do_Gry['5'] == Plansza_Do_Gry['7'] != ' ':
                    drukuj_plansze(Plansza_Do_Gry)
                    print('\nKoniec gry') 
                    print(f'WYGRAŁ GRACZ: {gracz}')
                    break