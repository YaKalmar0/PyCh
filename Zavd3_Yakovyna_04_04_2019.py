class GrandMom():
    def life(self):
        print("I remember my mom telling...")

class Mom(GrandMom):
    def hangout(self):
        print("We loved dancing and weed(ing)s.")

class Dad(GrandMom):
    def ninetieth(self):
        print("Racket was everything we had.")

class MeMyselfI(Mom, Dad):
    def memes(self):
        print("Just memes. Nothing more.")

G = GrandMom()
M = Mom()
D = Dad()
I = MeMyselfI()
print(type.mro(MeMyselfI))