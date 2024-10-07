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

fishers_pike = Weapon("Fisher's Pike", "Pointy", 18, 28)

fists = Weapon("Good Ol Left Hook", "Blunt", 7, 0)

#Ranged Weapons
thorned_bow = Weapon("Thorned Bow", "Ranged magic", 16, 25)

hunters_bow = Weapon("Hunter's bow", "Ranged", 12, 20)

