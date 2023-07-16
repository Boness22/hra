def pole():
    # Inicializace herního pole
    herni_pole = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    for i in herni_pole:
        print(i)


def game(hrac_1, hrac_2):
    # Inicializace herního pole
    herni_pole = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    cislo = 0


    while cislo < 10:
        # První hráč
        while True:
            vstup = input("Hráč_1, zadej cisla od 0 - 3:  ")
            try:
                vstup_hrace1 = [int(cislo) for cislo in vstup]
                radek = int(vstup_hrace1[0]) - 1
                sloupek = int(vstup_hrace1[1]) - 1
                
                # Kontrola platnosti tahu hráče 1
                if game_rules_player1(radek, sloupek, herni_pole, hrac_1) == True:
                    break
                  
            except ValueError:
                print("zadej pouze čísla a bez mezer")

        # Druhy hráč
        while True:
            vstup = input("Hráč_2, zadej cisla od 0 - 3: ")
            try:
                vstup_hrace2 = [int(cislo) for cislo in vstup]
                radek = int(vstup_hrace2[0]) - 1
                sloupek = int(vstup_hrace2[1]) - 1

                # Kontrola platnosti tahu hráče 2
                if game_rules_player2(radek,sloupek,herni_pole, hrac_2) == True:
                    break
               
            except ValueError:
                print("zadej pouze čísla a bez mezer")

        #  pricitani opakovani
        cislo += 1
        

def player_one():
    hrac1 = input("Hráč1 zvol si symbol: ")
    return hrac1


def player_two():
    hrac2 = input("Hráč2 zvol si symbol: ")
    return hrac2


def game_rules_player1(radek, sloupek, herni_pole, hrac_1):
    if herni_pole[radek][sloupek] == "_":
        # Přidání symbolu hráče 1 na herní pole
        herni_pole[radek][sloupek] = hrac_1
        
        # Výpis herního pole po tahu hráče 1
        for i in herni_pole:
            print(i)  
        
        return True  # Platný tah               
                    
    else:
        print("Toto pole je již obsazené. Zkus to znovu.")
        return False  # Neplatný tah


def game_rules_player2(radek,sloupek, herni_pole, hrac_2):
    if herni_pole[radek][sloupek] == "_":

        # Pridání symbolu hráče 2 na herní pole
        herni_pole[radek][sloupek] = hrac_2

        # Výpis herního pole po tahu hráče 2
        for i in herni_pole:
            print(i)
        # platný tah
        return True 

    else:
        print("Toto pole je již obsazené")
        # neplatný tah
        return False    


def win():
    # Logika pro zjištění vítěze
    pass






hrac_1 = player_one()
hrac_2 = player_two()
game(hrac_1, hrac_2)