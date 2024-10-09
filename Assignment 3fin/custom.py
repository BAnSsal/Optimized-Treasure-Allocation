
from treasure import Treasure

class Bigtr:
    
    
    def __init__(self, treas):
        self.priority = treas.size+treas.arrival_time
        self.mytreasure=treas
    
    