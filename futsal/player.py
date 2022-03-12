from .bll import BaseObject

class Player(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)