class Human:
    species = "sapiens"
    
    def __init__(self, age=None):
        self._age = None  # Initialize the private attribute
        if age is not None:
            self.age = age  # Use the property setter for validation

    def get_age(self):
        print("Retrieving age")
        return self._age
    
    def set_age(self, age):
        if isinstance(age, (int, float)) and 0 <= age <= 120:
            print(f"Setting age to {age}")
            self._age = age  # Set the private attribute directly
        else:
            print("Age must be a number between 0 and 120")
            
    age = property(get_age, set_age)

# Function to get a valid age from the terminal
def input_age():
    while True:
        try:
            age_input = input("Please enter an age: ")
            age = float(age_input)
            if age.is_integer():
                age = int(age)
            if 0 <= age <= 120:
                return age
            else:
                print("Age must be between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Create a Human instance with age input from the terminal
age = input_age()
guido = Human(age=age)

# Example usage with terminal input
print(guido.age)
