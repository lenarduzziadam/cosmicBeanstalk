import pygame, sys
from config import *
from character import Hero, Enemy
from weapon import *

chosen = Hero(name= "Arshan", health = 150)
chosen.equip(uchigatana)

boss = Enemy(name = "Todokhin", health = 300, weapon = steel_longsword)
grunt = Enemy("Goblin Acolyte", health = 50, weapon = fishers_pike)

while True:
    chosen.attack(boss)
    boss.attack(chosen)
    
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {boss.name}: {boss.health}" )
    
    chosen.attack(boss)
    boss.attack(chosen)
    grunt.attack(chosen)
    
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {boss.name}: {boss.health}" )
    
    chosen.attack(grunt)
    boss.attack(chosen)
    
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {grunt.name}: {grunt.health}" )
    
    chosen.drop()
    
    input()