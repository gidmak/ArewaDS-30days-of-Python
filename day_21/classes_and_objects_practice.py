# This is for practicing python classes and objects

# Create a class
class Person:
    def __init__(self, name):
        # self allows parameters to be added to the class
        self.name = name

p = Person("Gideon")
print(p)
print(p.name)

# Adding more parameters to the class
class Person:
    def __init__(self, firstname, middlename, lastname, age, country, job_status):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.age = age
        self.country = country
        self.job_status = job_status
    
    def person_info(self):
        return f"{self.firstname} {self.middlename} {self.lastname} is {self.age} years old. He lives in {self.country} and is {self.job_status}"
    
# Create an instance of the person class
p = Person("Gideon", "Yashim", "Markus", 34, "Nigeria", "Employed")

# Print the person information
print(p.person_info())

