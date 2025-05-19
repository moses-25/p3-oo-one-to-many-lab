class Pet:
    PET_TYPES = ["Dog", "Cat", "Rodent", "Bird", "Reptile", "Exotic"]
    all = []
    def __init__(self, name, pet_type, owner = None):
        if pet_type not in pet.PET_TYPES:
            raise Exception(f"Invalid pet type")
        self.pet_type = pet_type
        self.name = name
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pet(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(self, pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pet(), key=lambda pet: pet.name)