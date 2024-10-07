import pygame, sys
from config import *
from character import *
from weapon import *
from healthbar import *

chosen = Hero(name= "Arshan", health = 500)
chosen.equip(uchigatana)

boss = Enemy(name = "Todokhin", health = 300, weapon = steel_longsword)
grunt = Enemy("Goblin Acolyte", health = 50, weapon = fishers_pike)

while True:
    chosen.attack(boss)
    boss.attack(chosen)
    
    chosen.healthbar.draw()
    boss.healthbar.draw()
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {boss.name}: {boss.health}" )
    
    chosen.attack(boss)
    boss.attack(chosen)
    grunt.attack(chosen)
    
    chosen.healthbar.draw()
    boss.healthbar.draw()
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {boss.name}: {boss.health}" )
    
    chosen.attack(grunt)
    boss.attack(chosen)
    
    chosen.healthbar.draw()
    grunt.healthbar.draw()
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {grunt.name}: {grunt.health}" )
    
    if chosen.weapon != fists:
        chosen.drop()
    
    input()