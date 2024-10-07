# main.py
import pygame, sys
from config import *
from character import Hero, Enemy
from weapon import *

chosen = Hero(name= "Arshan", health = 150)
chosen.equip(uchigatana)

enemy = Enemy(name = "Todokhin", health = 300, weapon = steel_longsword)

while True:
    chosen.attack(enemy)
    enemy.attack(chosen)
    
    print(f"health of {chosen.name}: {chosen.health}" )
    print(f"health of {enemy.name}: {enemy.health}" )
    
    chosen.drop()
    
    input()