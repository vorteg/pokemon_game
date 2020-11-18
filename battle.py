from battle_constants import *

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0
        
    def is_finished(self):
        finished = self.pokemon1.current_hp <= 0  or self.pokemon2.current_hp <= 0
        if finished:
            self.print_winner()
        return finished
    
    def execute_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        attack1 = None
        attack2 = None
        if DO_ATTACK in command1.action.keys():
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]
            
        #Damage Formula
        self.pokemon2.current_hp -= attack1.power
        self.pokemon1.current_hp -= attack2.power
        
        self.actual_turn += 1
        
    def print_winner(self):
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp:
            print(self.pokemon2.name + " won in  " + str(self.actual_turn) + "  turns!!")
        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp:
            print(self.pokemon1.name + " won in  " + str(self.actual_turn) + "  turns!!")
        else:
            print("Double KO!!")
    
    def print_current_status(self):
        print(self.pokemon1.name + " has " + str(self.pokemon1.current_hp) + " left!")
        print(self.pokemon2.name + " has " + str(self.pokemon2.current_hp) + " left!")