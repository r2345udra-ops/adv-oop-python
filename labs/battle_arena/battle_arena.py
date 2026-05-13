import random

class InvalidDamageError(Exception):
    pass


class AttackEffect:
    def apply(self, target: Character):
        raise NotImplementedError
    
class PoisonEffect(AttackEffect):
    def apply(self, target):
        target.take_damage(5)
    

class FreezeEffect(AttackEffect):
    def apply(self, target):
        print(f"{target.name} is frozen")
        
class Player:
    def __init__(self, username):
        self._username = username


class Character:
    def __init__(self, name, health, attack_strategy):
        
        self._name = name
        self._health = health
        self._attack_strategy = attack_strategy #number of health points to reduce
        self._effects = effects        
        

    def attack(self, target: Character):
       self._attack_strategy.execute(self, target)
       
    
    def take_damage(self, damage):
        if damage < 0:
            raise InvalidDamageError("Damage cannot be negative")
        
        self._health -= damage
    
    
    def is_alive(self):
        return self._health > 0
    
    @property
    def name(self):
        return self._name 
    
    @property
    def attack_strategy(self):
        return self._attack_strategy
    
    @attack_strategy.setter
    def attack_strategy(self, value):
        self._attack_strategy = value
    
        
class AttackStrategy:
    def __init__(self, effects=None):
        self._effects = effects
        
    def execute(self, attacker: Character, target: Character):
        if self._effects:
           for effect in self._effects:
               effect.apply(target)


class SwordAttack(AttackStrategy):
    def execute(self, attacker, target):
        target.take_damage(25)
        super().execute(attacker, target) 
    
        


class FireballAttack(AttackStrategy):
    def execute(self, attacker, target):
        target.take_damage(40)
        super().execute(attacker, target) 
        

class CriticalStrike(AttackStrategy):
    def execute(self, attacker, target):
        damage = 20
        if random.random() < 0.3:
            damage *= 2
        
        target.take_damage(damage)
        super().execute(attacker, target)        
    



    
    
class Warrior(Character):
    
    def attack(self, target: Character):
        target.take_damage(40)

class Mage(Character):
    
    def attack(self, target: Character):
        target.take_damage(25)
        

class Archer(Character):
    def attack(self, target: Character):
        target.take_damage(15)
    




class Battle:
    
    def __init__(self, figher_one: Character,  fighter_two: Character):
        self._fighter_one = figher_one
        self._fighter_two = fighter_two
        self._winner = None
        self._is_finished = False
        self._turn =  1
    
    @property
    def winner(self):
        return self._winner
    
    @property
    def is_finished(self):
        return self._is_finished 
    
    def start(self):
        print("Starting the battle")
        
        while not self._is_finished:
            self.perfom_turn()
        
        

    def perfom_turn(self):
        self._fighter_one.attack(self._fighter_two)
        
        if not self._fighter_two.is_alive():
            self._winner = self._fighter_one
            self._is_finished = True
            return 
        
        self._fighter_two.attack(self._fighter_one)    
        
        if not self._fighter_one.is_alive():
            self._winner = self._fighter_two
            self._is_finished = True
            return
        
        self._turn += 1

        






if __name__ == "__main__":
    
    warrior = Warrior("Warrior", 100, SwordAttack())
    
    mage = Mage("Mage", 75,  FireballAttack())
    
    battle  = Battle(warrior, mage)
    
    
    battle.start()
    
    print(battle.winner.name)
    
  
    
    
    
     
    
