from random import randint

class MorpionGame:
    def __init__(self):
        self.casesColor = [None, None, None, None, None, None, None, None, None]
        self.casesSize = [None, None, None, None, None, None, None, None, None]
        self.cases = [None, None, None, None, None, None, None, None, None]
        self.white_pawns = [2, 2, 2]
        self.black_pawns = [2, 2, 2]
        self.winner = None
        self.count = 0
        self.player = "w"
        self.state = "playing"

    def get_visual(self, case):
        if self.cases[case-1] == None:
            return ""
        if self.casesSize[case-1] == 0:
            return "◽" if self.casesColor[case-1] == "w" else "◾"
        if self.casesSize[case-1] == 1:
            return "◻️" if self.casesColor[case-1] == "w" else "◼️"
        if self.casesSize[case-1] == 2:
            return "⬜" if self.casesColor[case-1] == "w" else "⬛"
        return ""
    
    def check_winner(self):
        p = ["123", "456", "789", "147", "258", "369", "159", "357"]
        for i in p:
            if self.casesColor[int(i[0])-1] == self.casesColor[int(i[1])-1] == self.casesColor[int(i[2])-1] != None:
                self.winner = self.player
        if self.winner == None:
            if self.black_pawns[0] + self.black_pawns[1] + self.black_pawns[2] == 0:
                self.winner = "nul"
            elif all(case is not None for case in self.cases):
                if ((self.white_pawns[0] + self.black_pawns[0]) <= 3) and (self.white_pawns[1] + self.black_pawns[1] + self.white_pawns[2] + self.black_pawns[2] == 0):
                    self.winner = "nul"
            else:
                self.winner = None
        return self.winner

    def can_pose(self, case, size):
        if size == 0 and self.cases[case-1] == None and self.white_pawns[0] > 0:
            return True
        elif size == 1 and (self.casesSize[case-1] == 0 or self.cases[case-1] == None) and self.white_pawns[1] > 0:
            return True
        elif size == 2 and (self.casesSize[case-1] == 0 or self.casesSize[case-1] == 1 or self.cases[case-1] == None) and self.white_pawns[2] > 0:
            return True
        else:
            return False
        
    def can_black_pose(self, case, size):
        if size == 0 and self.cases[case-1] == None and self.black_pawns[0] > 0:
            return True
        elif size == 1 and (self.casesSize[case-1] == 0 or self.cases[case-1] == None) and self.black_pawns[1] > 0:
            return True
        elif size == 2 and (self.casesSize[case-1] == 0 or self.casesSize[case-1] == 1 or self.cases[case-1] == None) and self.black_pawns[2] > 0:
            return True
        else:
            return False

    def add_pawn(self, case, size, color):
        self.casesColor[case-1] = color
        self.casesSize[case-1] = size
        self.cases[case-1] = color + str(size)
        if color == "w":
            self.white_pawns[size] -= 1
        else:
            self.black_pawns[size] -= 1

    def switch_player(self):
        self.player = ("w" if self.player == "b" else "b")
        self.count += 1

    def player_turn(self, case, size):
        if size == 0 and self.cases[case-1] == None and self.white_pawns[0] > 0:
            self.add_pawn(case, 0, "w")
        elif size == 1 and (self.casesSize[case-1] == 0 or self.cases[case-1] == None) and self.white_pawns[1] > 0:
            self.add_pawn(case, 1, "w")
        elif size == 2 and (self.casesSize[case-1] == 0 or self.casesSize[case-1] == 1 or self.cases[case-1] == None) and self.white_pawns[2] > 0:
            self.add_pawn(case, 2, "w")
        else:
            return False
        self.switch_player()
        return self.cases[case-1]
    
    def black_player_turn(self, case, size):
        if size == 0 and self.cases[case-1] == None and self.black_pawns[0] > 0:
            self.add_pawn(case, 0, "b")
        elif size == 1 and (self.casesSize[case-1] == 0 or self.cases[case-1] == None) and self.black_pawns[1] > 0:
            self.add_pawn(case, 1, "b")
        elif size == 2 and (self.casesSize[case-1] == 0 or self.casesSize[case-1] == 1 or self.cases[case-1] == None) and self.black_pawns[2] > 0:
            self.add_pawn(case, 2, "b")
        else:
            return False
        self.switch_player()
        return self.cases[case-1]

    def ia_turn(self):
        bot_played = False
        p = ["123", "456", "789", "147", "258", "369", "159", "357"]

        # Etape 1 : Verifier si le bot peut gagner
        # si oui, le bot joue de manière à gagner
        for j in p:
            j *= 2
            for i in range(3):
                if self.casesColor[int(j[0+i])-1] == self.casesColor[int(j[1+i])-1] == "b" and self.cases[int(j[2+i])-1] != "w2" and not bot_played:
                    if self.cases[int(j[2+i])-1] == None:
                        if self.black_pawns[0] > 0:
                            self.add_pawn(int(j[2+i]), 0, "b")
                            bot_played = True
                        elif self.black_pawns[1] > 0:
                            self.add_pawn(int(j[2+i]), 1, "b")
                            bot_played = True
                        elif self.black_pawns[2] > 0:
                            self.add_pawn(int(j[2+i]), 2, "b")
                            bot_played = True
                    elif self.cases[int(j[2+i])-1] == "w0":
                        if self.black_pawns[1] > 0:
                            self.add_pawn(int(j[2+i]), 1, "b")
                            bot_played = True
                        elif self.black_pawns[2] > 0:
                            self.add_pawn(int(j[2+i]), 2, "b")
                            bot_played = True
                    elif self.cases[int(j[2+i])-1] == "w1" and self.black_pawns[2] > 0:
                        self.add_pawn(int(j[2+i]), 2, "b")
                        bot_played = True

        # Etape 2 : Si le bot ne peut pas gagner et que le joueur peut gagner :
        # Le bot empèche le joueur de gagner
        for j in p:
            j *= 2
            for i in range(3):
                # 1 = j[0+i] ; 2 = j[1+i] ; 3 = j[2+i]
                if self.casesColor[int(j[0+i])-1] == self.casesColor[int(j[1+i])-1] == "w" and self.cases[int(j[2+i])-1] != "b2" and not bot_played:
                    if self.cases[int(j[2+i])-1] == None:
                        if self.black_pawns[2] > 0:
                            self.add_pawn(int(j[2+i]), 2, "b")
                            bot_played = True
                        elif self.black_pawns[1] > 0:
                            self.add_pawn(int(j[2+i]), 1, "b")
                            bot_played = True
                        else:
                            self.add_pawn(int(j[2+i]), 0, "b")
                            bot_played = True
                    elif self.cases[int(j[2+i])-1] == "b1":
                        if self.black_pawns[2] > 0:
                            self.add_pawn(int(j[2+i]), 2, "b")
                            bot_played = True
                    elif self.cases[int(j[2+i])-1] == "b0":
                        if self.black_pawns[2] > 0:
                            self.add_pawn(int(j[2+i]), 2, "b")
                            bot_played = True
                        elif self.black_pawns[1] > 0:
                            self.add_pawn(int(j[2+i]), 1, "b")
                            bot_played = True

        # Etape 3 : Si ni le joueur ni le bot peuvent gagner,
        # jouer de manic̀re stratégique comme au centre ou sur un coin 
        m = "51379"
        for i in m:
            i = int(i)
            if self.cases[i-1] == None and self.black_pawns[0] > 0 and not bot_played:
                self.add_pawn(i, 0, "b")
                bot_played = True
            elif self.cases[i-1] == "w0" and not bot_played:
                if self.black_pawns[1] > 0:
                    self.add_pawn(i, 1, "b")
                    bot_played = True
                elif self.black_pawns[2] > 0:
                    self.add_pawn(i, 2, "b")
                    bot_played = True

        # Etape 4 : Sinon, jouer aléatoirement
        random_case = randint(0, 8)
        random_size = randint(0, 2)

        bot_error = True

        while not bot_error:
            if random_size == 0 and self.cases[random_case] == None and self.black_pawns[0] > 0 and not bot_played:
                self.add_pawn(random_case+1, 0, "b")
                bot_played = True
                bot_error = False
            elif random_size == 1 and (self.casesSize[random_case] == 0 or self.cases[random_case] == None) and self.black_pawns[1] > 0 and not bot_played:
                self.add_pawn(random_case+1, 1, "b")
                bot_played = True
                bot_error = False
            elif random_size == 2 and (self.casesSize[random_case] == 0 or self.casesSize[random_case] == 1 or self.cases[random_case] == None) and self.black_pawns[2] > 0 and not bot_played:
                self.add_pawn(random_case+1, 2, "b")
                bot_played = True
                bot_error = False

        self.switch_player()