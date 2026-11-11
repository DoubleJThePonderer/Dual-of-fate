import random #vi bruker random for fiendene sin "ai"

class Entity:
    def __init__(self, actions:list, hp:int):
        self.actions = actions
        self.hp = hp

class Player(Entity):
    def __init__(self):
        super().__init__()

    def regen(self):
        self.hp += 50 - self.hp / 2 # regen er større jo mindre hp du har

class Boss(Entity):
    def __init__(self, actions, hp):
        super().__init__(actions, hp)
    
    def xFactor():
        pass

class Actions():
    def __init__(self, value, cooldown):
        self.val = value
        self.cd = cooldown
        
        
entity1 = Entity(["Attack", "Defend"], 100)
player1 = Player(["Run", "Jump", "Heal"], 150)

