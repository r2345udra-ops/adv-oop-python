from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, attacker_name):
        pass
    
    
class DefenseStrategy(ABC):
    @abstractmethod
    def defend(self, defender_name):
        pass
    
class SpecialAbilityStrategy(ABC):
    @abstractmethod
    def use_ability(self, user_name):
        pass
    

class ChargeAttack(AttackStrategy):
    """Aggressive close-range attack - Orc style"""
    
    def attack(self, attacker_name):
        print(f"⚔️  {attacker_name} charges forward with an axe!")
        print(f"   Damage dealt: HIGH (30)")
        return 30

class RangedAttack(AttackStrategy):
    """Ranged attack from distance - Elf style"""
    
    def attack(self, attacker_name):
        print(f"🏹 {attacker_name} fires arrows from a distance!")
        print(f"   Damage dealt: MEDIUM (10)")
        return 10

class FirebreathAttack(AttackStrategy):
    """Area attack - Dragon style"""
    
    def attack(self, attacker_name):
        print(f"🔥 {attacker_name} breathes fire, engulfing the area!")
        print(f"   Damage dealt: CRITICAL (50)")
        return 50

class SneakAttack(AttackStrategy):
    """Backstab attack - Goblin style"""
    
    def attack(self, attacker_name):
        print(f"🗡️  {attacker_name} emerges from shadows and backstabs!")
        print(f"   Damage dealt: MEDIUM (20)")
        return 20



class BruteForceDefense(DefenseStrategy):
    """Tank damage - Orc style"""
    
    def defend(self, defender_name) -> int:
        print(f"🛡️  {defender_name} braces for impact")
        damage_taken = 20
        print(f"   Damage taken: {damage_taken}")
        return damage_taken

class NimbleDefense(DefenseStrategy):
    """Dodge and evade - Elf style"""
    
    def defend(self, defender_name) -> int:
        print(f"💨 {defender_name} nimbly dodges")
        damage_taken = 10
        print(f"   Damage taken: {damage_taken}")
        return damage_taken

class ScaledDefense(DefenseStrategy):
    """Natural armor - Dragon style"""
    
    def defend(self, defender_name) -> int:
        print(f"🐉 {defender_name}'s scales absorb most damage")
        damage_taken = 5
        print(f"   Damage taken: {damage_taken}")
        return damage_taken

class FragileDefense(DefenseStrategy):
    """No armor - Goblin style"""
    
    def defend(self, defender_name) -> int:
        print(f"⚠️  {defender_name} has no protection!")
        damage_taken = 25
        print(f"   Damage taken: {damage_taken}")
        return damage_taken



class Intimidate(SpecialAbilityStrategy):
    """Orc ability"""
    
    def use_ability(self, user_name):
        print(f"😤 {user_name} roars and intimidates enemies!")

class Camouflage(SpecialAbilityStrategy):
    """Elf ability"""
    
    def use_ability(self, user_name):
        print(f"👻 {user_name} blends into the environment!")

class TimeWarp(SpecialAbilityStrategy):
    """Dragon ability"""
    
    def use_ability(self, user_name):
        print(f"⏳ {user_name} bends time!")

class Replicate(SpecialAbilityStrategy):
    """Goblin ability"""
    
    def use_ability(self, user_name):
        print(f"📋 {user_name} multiplies into 3 copies!")



 



# Before strategy
# class Enemy:
#     def __init__(self, name, enemy_type, health):
#         self.name = name
#         self.enemy_type = enemy_type # orc, elf, dragon ,goblin
#         self.health = health
#         self.player_distance = 100

#     def attack(self):
#         if self.enemy_type == "orc":
#             print(f"{self.name} charges forward with an axe!")
#             self.player_distance -= 30
#         elif self.enemy_type == "elf":
#             print(f"{self.name} fires arrows from a distance!")
#             self.player_distance -= 10  # Less damage
#         elif self.enemy_type == "dragon":
#             print(f"{self.name} breathes fire!")
#             self.player_distance -= 50
#         elif self.enemy_type == "goblin":
#             print(f"{self.name} sneaks and backstabs!")
#             self.player_distance -= 20
#         elif self.enemy_type == "zombie":
#             print(f"{self.name} slowly lurches forward!")   
        
    
#     def defend(self):
#         if self.enemy_type == "orc":
#             # Orcs don't defend well
#             self.health -= 20
#         elif self.enemy_type == "elf":
#             # Elves are nimble
#             self.health -= 10
#         elif self.enemy_type == "dragon":
#             # Dragons have thick scales
#             self.health -= 5
#         elif self.enemy_type == "goblin":
#             # Goblins are fragile
#             self.health -= 25
            
#         elif self.enemy_type == "zombie":
#             self.health -= 15
    
    
#     def use_special_ability(self):
#         if self.enemy_type == "orc":
#             print(f"{self.name} roars to intimidate!")
#         elif self.enemy_type == "elf":
#             print(f"{self.name} uses camouflage!")
#         elif self.enemy_type == "dragon":
#             print(f"{self.name} uses time warp!")
#         elif self.enemy_type == "goblin":
#             print(f"{self.name} multiplies into 3 goblins!")
#         elif self.enemy_type == "zombie":
#             print(f"{self.name} infects the player!")
            


# With strategy
class Enemy:
    def __init__(self, name, health, 
                 attack_strategy: AttackStrategy,
                 defense_strategy: DefenseStrategy,
                 ability_strategy: SpecialAbilityStrategy):
        self.name = name
        self.health = health
        self.player_distance = 100
        self.attack_strategy = attack_strategy
        self.defense_strategy = defense_strategy
        self.ability_strategy = ability_strategy

    def attack(self):
        damage = self.attack_strategy.attack(self.name)
        return damage
        
    
    def defend(self):
        damage_taken = self.defense_strategy.defend(self.name)
        self.health -= damage_taken
        
        
    
    
    def use_special_ability(self):
       self.ability_strategy.use_ability(self.name)

# orc = Enemy("Uruk", "orc", 100)
# orc.attack()
# orc.defend()
# orc.use_special_ability()

charge = ChargeAttack()
ranged = RangedAttack()
firebreath = FirebreathAttack()
sneak = SneakAttack()


brute_defense = BruteForceDefense()
nimble_defense = NimbleDefense()
scaled_defense = ScaledDefense()
fragile_defense = FragileDefense()

intimidate = Intimidate()
camouflage = Camouflage()
time_warp = TimeWarp()
replicate = Replicate()

print("=== Creating Enemies ===\n")

orc = Enemy("Grommash", 100, charge, brute_defense, intimidate)
elf = Enemy("Legolas", 80, ranged, nimble_defense, camouflage)
dragon = Enemy("Smaug", 150, firebreath, scaled_defense, time_warp)
goblin = Enemy("Sneaky", 50, sneak, fragile_defense, replicate)

orc.attack()
orc.defend()
orc.use_special_ability()