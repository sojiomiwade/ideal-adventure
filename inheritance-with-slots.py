class Mammal:
    def __init__(self,mamm_glands='white') -> None:
        self.mamm_glands=mamm_glands

class LandAnimal:
    def __init__(self,lungs=2) -> None:
        self.lungs=lungs

class Dog(LandAnimal,Mammal):
    def __init__(self,bark) -> None:
        super().__init__()
        # print('super',a.legs)
        self.bark=bark

        try:
            self.mamm_glands
        except AttributeError:
            print('no mamm glands')

        try:
            self.lungs
        except AttributeError:
            print('no lungs')

d=Dog(bark='loud')
# print(d.bark)
# print(type(super(Dog,d)))