import os

os.system("")

class HealthBar:
    symbol_remain: str = "#"
    symbol_lost: str = "_"
    barrier: str = "|"
    
    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        
        self.is_colored = is_colored
        self.color = color
        
        