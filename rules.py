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

