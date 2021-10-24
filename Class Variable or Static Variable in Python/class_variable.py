# Class Variable or Static Variable in Python
# class Mobile:
#     fp = "yes"          # Class Variable

#     @classmethod
#     def is_fp(cls):
#         print(cls.fp)

# realme = Mobile()
# print(Mobile.fp)
# Mobile.is_fp()


class Mobile:
    fp = "yes"          # Class Variable

    def __init__(self):
        self.model = "Realme X"

    def show_model(self):
        print(f"Model: {self.model}")

    @classmethod
    def is_fp(cls):
        print(f"Finger Print: {cls.fp}")        #Accessing class variable


realme = Mobile()
realme.show_model()
Mobile.is_fp()

print()

Mobile.fp = "No"            # modifying class variable

realme = Mobile()
realme.show_model()
Mobile.is_fp()
