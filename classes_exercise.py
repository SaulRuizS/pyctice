class Person:                         #Pascal notation for classes (caps letters at the begining of the name)
    def __init__(self, age):            #This is the constructor, __init__ means the initialation of the object
        self.age = age                  #"self" represents the object, in this case is taking the argument to define an attribute
    
    def talk(self, phrase):             
        print("You said:", phrase) 


age = input("Introduce your age: ")
person = Person(age)                    #The object is initialazed so the constructor is executed with argument age
print("Your age is", person.age)        #Prints the new assigned attribute

phrase = input("Something that you want to say? ")
person.talk(phrase)

#-------------INHERITANCE----------------

class Male(Person):
    pass


class Female(Person):
    pass


class Other(Person):
    identifier = ""


male = Male(34)
print(male.age)

female = Female(27)
print(female.age)

other = Other(1000)
other.identifier = "Semi God"
print(other.age, "\n",other.identifier)