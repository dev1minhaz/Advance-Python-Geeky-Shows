# Instance Method in Python

# class Mobile:
#     def __init__(self):
#         self.model = "Realme X"
#     # instance method
#     def show_model(self):
#         print(f"Model: {self.model}")


# realme = Mobile()
# realme.show_model()


class Mobile:
    def __init__(self):
        self.model = "Realme X"
    # instance method
    def show_model(self, p):
        self.price = p
        print(f"Model: {self.model}, Price: {self.price}")


realme = Mobile()
redmi = Mobile()
realme.show_model(1000)
realme.show_model(2000)
