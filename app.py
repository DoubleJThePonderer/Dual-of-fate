import random #vi bruker random for fiendene sin "ai"
from __future__ import annotations

class Entity:
    def __init__(self, actions:list, hp:int):
        self.actions = actions
        self.hp = hp

class Player(Entity):
    def __init__(self):
        super().__init__()

    def regen(self):
        self.hp += 75 - self.hp // 2 # regen er større jo mindre hp du har

class Boss(Entity):
    def __init__(self, actions, hp):
        super().__init__(actions, hp)
    
    def xFactor():
        pass

class Actions():
    def __init__(self, value:int, cooldown:int, target:object):
        self.val = value
        self.cd = cooldown
        self.target = target
    
    def activate(self):
        self.target.hp -= self.val # skade/heal gøres her
        
# alle entities
boss = Boss([], 200)
entity1 = Entity([], 100)
player1 = Player([], 150)
# alle actions
playH = Actions(-50, 5, player1)
playA = Actions(10, 0, entity1 or boss)
playK = Actions(20,2, entity1 or boss)
enyA = Actions(10, 0, player1)
enyK = Actions(20, 0, player1)
# legger alle actions i entities
player1.actions.append[playA,playK,playH]
entity1.actions.append[enyA,enyK]

while player1.hp > 0:
    print("")
    while entity1.hp > 0:
        print(f"du har {player1.hp} liv")
        action = (input(f"What action do you want to use. {player1.actions}"))
        if action in player1.actions:
            player1.action.activate()
            
