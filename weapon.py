class Weapon:
    def __init__(self, 
                 name: str, 
                 weapon_type: str, 
                 element: str,
                 damage: int, 
                 value: int
                 ) -> None:
        
        self.name = name
        self.weapon_type = weapon_type
        self.element = element
        self.damage = damage
        self.value = value
        
#Weapon Classifications

#Melee Weapons
uchigatana = Weapon("Uchigatana", "Sharp curved", "N/a", 29, 42)

steel_longsword = Weapon("Steel Longsword", "Sharp", "N/a", 20, 30)

drake_slayer = Weapon("Drakeslayer", "Blunt", "dragon", 70, 500)

fishers_pike = Weapon("Fisher's Pike", "Pointy", "N/a", 18, 28)

giants_hooks = Weapon("Hook of a Giant", "Pointy curved", "arcane", 24, 35)

fists = Weapon("Good Ol Left Hook", "Blunt", "N/a", 7, 0)


#Ranged Weapons
thorned_bow = Weapon("Thorned Bow", "Ranged magic", "Earth", 16, 25)

hunters_bow = Weapon("Hunter's bow", "Ranged", "N/a", 12, 20)


#spellcasting
sumer_rage = Weapon("Rage of Sumeria", "AoE Spell", "earth", 60, 150)

gilgamesh_fall = Weapon("Fall of Gilgamesh", "Ranged Spell", "earth", 75, 700)

water_reflect = Weapon("Waters Reflection", "Melee Spell", "water", 40, 70)

enflamed_kasenaru = Weapon("Enflamed Kasenaru", "Ranged Spell", "fire", 50, 130)

stalking_vines = Weapon("Vines of the Great Stalk", "Ranged Spell", "arcane", 80, 1000)

wolfs_moon = Weapon("Howlers Moon", "AoE Spell", "cosmic", 45, 650)


class Weakness:
    def __init__(self, type: str, multiplier: int): 
        self.type = type
        self.multiplier = multiplier
        
#Magic elemental weakness    
fire = Weakness("fire", 2)
water = Weakness("water", 2)
earth = Weakness("earth", 2)

arcane = Weakness("arcane", 3)
cosmic = Weakness("cosmic", 3)

#Damage type weakness
sharp = Weakness("Sharp", 2)
blunt = Weakness("Blunt", 2)
pointy = Weakness("Pointy", 2)

ranged = Weakness("Ranged", 3)