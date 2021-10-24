# class Mobile:
#     def __init__(self):
#         print("Mobile Constructor Called")

# realme = Mobile()


# class Mobile:
#     def __init__(self):
#         self.model = "Realme X"
    
#     def show_model(self):
#         print(f"Model: {self.model}")

# realme = Mobile()
# realme.show_model()

class Mobile:
    def __init__(self, m, v=80):
        self.model = m
        self.volumn = v
    
    def show_model(self, p):
        price = p
        print(f"Model: {self.model}, Volumn: {self.volumn}, Price: {price}")

realme = Mobile("Realme X", 50)
realme.show_model(25000)

redmi = Mobile("Redmi XL")
redmi.show_model(25000)

print("testing")