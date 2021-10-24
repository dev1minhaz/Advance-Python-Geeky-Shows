# Example 2

# class Myclass(object):
#     def show(self):
#         print("I am a Method")

# x = Myclass()
# x.show()


# Example 3
class Mobile:
    def __init__(self, m):
        self.model = m
    
    def show_model(self, p):
        price = p
        print(f"Model: {self.model}, Price: {price}")

realme = Mobile("Realme X")
realme.show_model(120000)
print(id(realme))

redmi = Mobile("Redmi 7s")
redmi.show_model(2000)
print(id(redmi))

geek = Mobile("Python")
geek.show_model(2344546)
print(id(geek))