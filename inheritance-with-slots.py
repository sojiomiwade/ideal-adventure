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
# class Bat:
    __slots__=('chiro','bigear')
    def __init__(self,chiro: str,bigear: bool) -> None:
        super().__init__()
        self.chiro=chiro
        self.bigear=bigear

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
b=Bat('chiro-a',True)
print(b.chiro)
b.chiro='chiro-b'
print(b.chiro)
b.chiro='chiro-c'
b.bigear='43'
# b.fish=42
# print(b.fish)
# print(b.__dict__, type(b))
print(type(b))

'''
>>> Bat
__main__.Bat

>>> Bat.mro()
[__main__.Bat, object]

>>> Bat.__mro__
(__main__.Bat, object)

>>> type(b)
__main__.Bat

>>> type(b).__mro__
(__main__.Bat, object)
'''