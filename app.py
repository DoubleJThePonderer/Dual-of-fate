import random #vi bruker random for fiendene sin "ai"
import time # vi bruker time for å skape litt mer action

class Entity:
    def __init__(self, actions:list, hp:int):
        self.actions = actions
        self.hp = hp

class Player(Entity):
    def __init__(self, actions, hp):
        super().__init__(actions, hp)
        self.points = 0
    def regen(self):
        self.hp += 75 - self.hp // 2 # regen er større jo mindre hp du har

class Boss(Entity):
    def __init__(self, actions, hp):
        super().__init__(actions, hp)
        self.sliten = 1
    
    def xFactor(self):
        player1.hp -= self.sliten
        self.sliten += 1

class Actions():
    def __init__(self, value:int, cooldown:int, target:object):
        self.val = value
        self.cd = cooldown
        self.target = target
    def __str__(self):
        if self.val > 0:
            return f"gjør {self.val} dmg"
        elif self.val < 0:
            return f"hebreder deg for {self.val*-1}"
    
    def activate(self):
        self.target.hp -= self.val # skade/heal gøres her
        # når playern healer så stopper denne fra at spilern får mer hp en 150
        if isinstance(self.target, Player):
            self.target.hp = min(150, self.target.hp)
        # takk gpt for denne
        
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
bosA = Actions(30, 0, player1)
# legger alle actions i entities
player1.actions.extend([playA,playK,playH])
entity1.actions.extend([enyA,enyK])
boss.actions.extend([enyK, bosA])
# ordbøker til å bruke angrep
player1.actions = {
    "angrip": playA,
    "spark": playK,
    "heal": playH
}

while player1.hp > 0:
    print("Du går ut av døra men plutselig")
    time.sleep(2)
    print("en fiende kommer med en kiv å skal drepe deg")
    while entity1.hp > 0:
        print(f"du har {player1.hp} liv")
        action = (input(f"hva velger du å gjøre. {player1.actions}"))
        if action in player1.actions:
            player1.actions[action].activate()
            print(f"fienden har {entity1.hp} liv")
            a = random.randint(0,1)
            entity1.actions[a].activate()
            print(f"Han slo tilbake og du tokk skade")
            print(f"du healer {75 - player1.hp // 2} etter at han slo deg")
            player1.regen()
        else:
            print("noe er feil") # feil søking kode. gjir bedsjed om at noe gikk feil i koden.
        if entity1.hp <= 0:
            print(f"du slo fienden og fikk {100 + player1.hp} poeng")
            player1.points += 100 + player1.hp #du får mer poeng jo mer hp du slutter fighten med
    time.sleep(3)
    print("Etter kampen er du sliten, solen har gått ned.")
    time.sleep(2)
    print("over deg hører du. DU SKAL DØ NÅ")
    time.sleep(3)
    print("Sjefen har kommet til å gjøre jobben selv")
    while boss.hp > 0:
        print(f"du har {player1.hp} liv")
        action = (input(f"What action do you want to use. {player1.actions}"))
        if action in player1.actions:
            player1.actions[action].activate()
            print(f"Bossen har {boss.hp} liv")
            a = random.randint(0,1)
            boss.actions[a].activate()
            print("Han slo tilbake og du tokk skade")
            print(f"du healer {75 - player1.hp // 2} etter at han slo deg")
            player1.regen()
            print(f"du er sliten og tar {boss.sliten} skade")
            boss.xFactor()
        if boss.hp < 0:
            print(f"du slo bossen og fikk {200 + player1.hp} poeng")
            player1.points += 200 + player1.hp
            player1.hp = 0
print(f"spill over. Du fikk {player1.points} poeng")