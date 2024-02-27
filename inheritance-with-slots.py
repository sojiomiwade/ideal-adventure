class Animal:
    def __init__(self,movespeed: int=0) -> None:
        self.movespeed=movespeed

class Mammal(Animal):
    def __init__(self,breastsize: int=0) -> None:
        super().__init__()
        self.breastsize=breastsize

class WingedAnimal(Animal):
    def __init__(self, wingcount: int=0) -> None:
        super().__init__()
        self.wingcount=wingcount
        
class Bat(Mammal,WingedAnimal):
    def __init__(self,chiro: str) -> None:
        super().__init__()
        self.chiro=chiro

        try:
            self.chiro
        except:
            print('no chiro')

        try:
            self.wingcount
        except:
            print('no wingcount')

        try:
            self.movespeed
        except:
            print('no movespeed')

        try:
            self.breastsize
        except:
            print('no breastsize')
Bat('chiro-a')