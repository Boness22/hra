from rules import game_rules_player1, game_rules_player2
from board import init_herni_pole
from players import player_one, player_two


def game():
    herni_pole = init_herni_pole()

    hrac_1 = player_one()
    hrac_2 = player_two()

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

if __name__ == "__main__":
    game()
