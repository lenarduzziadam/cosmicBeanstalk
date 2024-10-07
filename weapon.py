class Weapon:
    def __init__(self, 
                 name: str, 
                 weapon_type: str, 
                 damage: int, 
                 value: int
                 ) -> None:
        
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        
#Weapon Classifications

#Melee Weapons
uchigatana = Weapon("Uchigatana", "Sharp curved", 29, 42)

steel_longsword = Weapon("Steel Longsword", "Sharp", 20, 30)

drake_slayer = Weapon("Drakeslayer", "Blunt", 70, 500)

fishers_pike = Weapon("Fisher's Pike", "Pointy", 18, 28)

giants_hooks = Weapon("Hook of a Giant", "Pointy curved", 24, 35)

fists = Weapon("Good Ol Left Hook", "Blunt", 7, 0)

#Ranged Weapons
thorned_bow = Weapon("Thorned Bow", "Ranged magic", 16, 25)

hunters_bow = Weapon("Hunter's bow", "Ranged", 12, 20)

#spellcasting
sumer_rage = Weapon("Rage of Sumeria", "AoE Spell", 60, 150)

gilgamesh_fall = Weapon("Fall of Gilgamesh", "Ranged Spell", 75, 700)

water_reflect = Weapon("Waters Reflection", "Melee Spell", 40, 70)


