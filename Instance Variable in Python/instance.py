# Instance Variable
class Mobile:
    def __init__(self):
        self.model = "Realme X"     # instance variable

    def show_model(self):
        print(self.model)       # accessing instance variable


realme = Mobile()
redmi = Mobile()
geek = Mobile()
print(realme.model)
print(redmi.model)
print(geek.model)

print()

redmi.model = "Redmi 7X"
print(realme.model)
print(redmi.model)
print(geek.model)
