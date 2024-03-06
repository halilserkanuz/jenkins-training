# List

people = ["Serkan", "Ahmet"]
for person in people:
    print(person)

people.sort()

for person in people:
    print(person)

people.append("Mehmet")
print(people)

people.insert(1, "Ali")
print(people)

people.extend(["Veli", "Hasan"])
print(people)

people.remove("Ali")
print(people)

people.pop()
print(people)


# Tuple

# Dict

applicant = {
    "name": "Serkan",
    "surname": "Yaren",
    "age": 25
}

for key, value in applicant.items():
    print(key, value)

from collections import OrderedDict

applicant = OrderedDict()

applicant["name"] = "Serkan"
applicant["surname"] = "Yaren"
applicant["age"] = 25