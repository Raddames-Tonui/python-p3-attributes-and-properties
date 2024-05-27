class Human:
    species = "Homo Sapiens"

    def __init__(self,age ):
        self.age = age
    
    def get_age(self ):
        print("Retrieving age!")
        return self._age 
    
    def set_age(self, age):
        if (type(age) in (int,float)) and( 0 <= age <= 120):
            print(f"Setting age to {age}")
            self._age =age
        
        else:
            print("Age must be a number between 0 and 120")

    age = property(get_age, set_age)

guido = Human(age=67)
# => Setting age to 67.
guido.age = 0
# => Setting age to 0.
guido.age = False
# => Age must be a number between 0 and 120
guido.age = 66
# => Setting age to 66.
guido.age
# => Retrieving age.
print(guido.age)
# => 66