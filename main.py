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