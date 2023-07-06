print("WELCOME TO THE VETERINARY CLINIC!")
import datetime
now = datetime.datetime.now()
print("Enter information about your pet")
pets = dict()
pet_name = input("Enter your pet's name: ")
pets_information = {"Pet's type": 0, "Pet's age": 0, "Pet's owner": 0}
pets[pet_name] = pets_information
pet_type = str(input("Enter the type of your pet: "))
pet_age = int(input("Enter your pet's year of birth (eg 2000): "))
pet_owner = str(input("Enter the name of the owner of the pet: "))
pets_information["Pet's type"] = pet_type
pets_information["Pet's age"] = now.year - pet_age
pets_information["Pet's owner"] = pet_owner
string = ""
if pets_information["Pet's age"] == 1:
    string = "year"
else:
    string = "years"
print("Pet Information:")
information = list(pets_information.values())
print("This is a", information[0], "named", str(*pets.keys()))
print("Pet age:", information[1], string)
print("Owner name:", information[2])
