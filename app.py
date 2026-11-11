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
        self.hp += 50 - self.hp / 2 # regen er større jo mindre hp du har

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
        self.target.hp -= self.val
        
        
entity1 = Entity(["Attack", "Defend"], 100)
player1 = Player(["Run", "Jump", "Heal"], 150)


while player1.hp > 0:
    action = (input(f"What action do you want to use. {player1.actions}"))
    if action in player1.actions:
        print(action)
