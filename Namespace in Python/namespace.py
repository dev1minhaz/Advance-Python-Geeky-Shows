# Namespace in Python

class Mobile:
    fp = "yes"      # class variable

    @classmethod    # class method
    def is_fp(cls):
        print(f"Finger Print: {cls.fp}")  # accessing class variable


realme = Mobile()
redmi = Mobile()
geek = Mobile()


print(f"Class FP: {Mobile.fp}")
print(f"Realme: {realme.fp}")
print(f"Redmi: {redmi.fp}")
print(f"Geek: {geek.fp}")

print()

Mobile.fp = "No"

print(f"Class FP: {Mobile.fp}")
print(f"Realme: {realme.fp}")
print(f"Redmi: {redmi.fp}")
print(f"Geek: {geek.fp}")

print()

realme.fp = "Not Working"

print(f"Class FP: {Mobile.fp}")
print(f"Realme: {realme.fp}")
print(f"Redmi: {redmi.fp}")
print(f"Geek: {geek.fp}")
