#constructor
class Person:
    def __init__(self, name, age, gender, occupation, addresa, vysku):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.addresa = addresa
        self.vysku = vysku

    def pozdrav(self):
        print(f"ahoj volam sa {self.name} a man {self.age} rokov ")
    def rod(self):
        print(f"som {self.gender}")
    def vydlisko(self):
        print(f"ahoj zijem v  {self.addresa} a mam {self.vysku}")
    def profesia(self):
        print(f" a som {self.occupation}")
    def zostarnem(self, cislo):
        self.age = self.age + cislo


allan = Person("Allan", 37, "muz", "Ekonom", "Bratislava", "1.67")
allan.pozdrav()
allan.vydlisko()
allan.profesia()
allan.rod()
print(allan.age)
allan.zostarnem(10)
print(allan.age)


