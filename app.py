age = int(input("Entrez votre âge : "))

if age < 18:
    print("Tu es mineur.")
elif age == 18:
    print("Tu es majeur.")
else:
    print("Tu es adulte.")