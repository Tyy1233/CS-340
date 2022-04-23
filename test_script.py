from animal_shelter import AnimalShelter
#object
shelter = AnimalShelter("accuser", "animals")
data = {"age_upon_outcome":"1.7 years", "animal_type": "cat"}
if shelter.create(data):
    print("animal added")