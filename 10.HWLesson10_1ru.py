print("Введите информацию о Вашем питомце")
pets = dict()
pet_name = input("Введите имя Вашего питомца: ")
pet_type = str(input("Введите вид Вашего питомца: "))
pet_age = int(input("Введите возраст Вашего питомца: "))
pet_owner = str(input("Введите имя владельца: "))
pets_information = dict()
pets_information["Pet's type"] = pet_type
pets_information["Pet's age"] = pet_age
pets_information["Pet's owner"] = pet_owner
pets[pet_name] = pets_information
string = ""
age = pets_information["Pet's age"]
if (age == 1):
    string = "год"
elif (age > 20) and (age % 10) == 1:
    string = "год"
elif (age > 0) and (age < 5):
    string = "года"
elif (age > 20) and ((age % 10) > 0) and ((age % 10) < 5):
    string = "года"
else:
    string = "лет"
print("Информация о питомце: ")
information = list(pets_information.values())
inf_of_pets = str(
    f'Это {information[0]} по кличке "{str(*pets.keys())}". Возраст питомца: {information[1]} {string}. Имя владельца: {information[2]}')
print(inf_of_pets)
