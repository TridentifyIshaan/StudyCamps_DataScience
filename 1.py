from datetime import datetime

# Person Class
class Person:
    def __init__(self, name: str, country: str, date_of_birth: str):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")  # Expecting date format 'YYYY-MM-DD'

    def calculate_age(self) -> int:
        today = datetime.today()
        age = today.year - self.date_of_birth.year

        # Adjust age if the person hasn't had their birthday yet this year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1

        return age

    def __repr__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}"

# Main Program
if __name__ == "__main__":
    # User input for creating a Person object
    name = input("Enter name: ")
    country = input("Enter country: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")

    # Creating a Person object with the provided input
    person = Person(name, country, dob)

    # Displaying the person's details and calculated age
    print(person)
    print(f"Age: {person.calculate_age()} years")