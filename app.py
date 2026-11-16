import random #vi bruker random for fiendene sin "ai"

class Entity:
    def __init__(self, actions:list, hp:int):
        self.actions = actions
        self.hp = hp

class Player(Entity):
    def __init__(self, actions, hp):
        super().__init__(actions, hp)

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
    def __str__(self):
        if self.val > 0:
            print(f"gjør {self.val} dmg")
        elif self.val < 0:
            print(f"hebreder deg for {self.val*-1}")
    
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
player1.actions.extend([playA,playK,playH])
entity1.actions.extend([enyA,enyK])

while player1.hp > 0:
    print("")
    while entity1.hp > 0:
        print(f"du har {player1.hp} liv")
        action = (input(f"What action do you want to use. {player1.actions}"))
        if action in player1.actions:
            player1.action.activate()
            print(f"fienden har {entity1.hp} liv")
            a = random.randint(1,2)
            entity1.actions[a].activate()
            print("fienden slo tilbake og du tokk skade")
            player1.regen()
            print("du healer etter at han slo deg")
