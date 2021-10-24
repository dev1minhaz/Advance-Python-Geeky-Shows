# Accessor or Getter Method and Mutator or Setter Method in Python
# class Mobile:
#     def __init__(self):
#         self.model = "Realme X"

#     def get_model(self):
#         return self.model

# realme = Mobile()
# m = realme.get_model()
# print(m)


class Mobile:
    # def __init__(self):
    #     self.model = "Realme X"

    def set_model(self, m):
        self.model = m


realme = Mobile()
realme.set_model("Huawei")
print(realme.model)