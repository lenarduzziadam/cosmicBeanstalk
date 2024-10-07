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
        self.damage = damage
        self.value = value
        
#Weapon Classifications

#Melee Weapons
uchigatana = Weapon("Uchigatana", "Sharp curved", "N/a", 29, 42)

steel_longsword = Weapon("Steel Longsword", "Sharp", "N/a", 20, 30)

drake_slayer = Weapon("Drakeslayer", "Blunt", "Dragon", 70, 500)

fishers_pike = Weapon("Fisher's Pike", "Pointy", "N/a", 18, 28)

giants_hooks = Weapon("Hook of a Giant", "Pointy curved", "Arcane", 24, 35)

fists = Weapon("Good Ol Left Hook", "Blunt", "N/a", 7, 0)

#Ranged Weapons
thorned_bow = Weapon("Thorned Bow", "Ranged magic", "Earth", 16, 25)

hunters_bow = Weapon("Hunter's bow", "Ranged", "N/a", 12, 20)

#spellcasting
sumer_rage = Weapon("Rage of Sumeria", "AoE Spell", "Earth", 60, 150)

gilgamesh_fall = Weapon("Fall of Gilgamesh", "Ranged Spell", "Earth", 75, 700)

water_reflect = Weapon("Waters Reflection", "Melee Spell", "water", 40, 70)

enflamed_kasenaru = Weapon("Enflamed Kasenaru", "Ranged Spell", "fire", 50, 130)


