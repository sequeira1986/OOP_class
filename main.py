#constructor
class Person:
    def __init__(self, name, age, gender, occupation, addresa, vysku, farba_oci):
        self.__nombre = name #el nombre senala a el atributo que definimos arriva
        self.__edad = age
        self.__gender = gender
        self.occupation = occupation
        self.addresa = addresa
        self.vysku = vysku
        self.farba_oci = farba_oci
    def pozdrav(self):
        print(f"ahoj volam sa {self.__nombre} a man {self.__edad} rokov , a mam {self.farba_oci} oci")
    def rod(self):
        print(f"som {self.__gender}")
    def vydlisko(self):
        print(f"ahoj zijem v  {self.addresa} a mam {self.vysku}")
    def profesia(self):
        print(f" a som {self.occupation}")
    def zostarnem(self, cislo):
        self.__edad = self.__edad + cislo
allan = Person("Allan", 37, "muz", "Ekonom", "Bratislava", "1.67", "hnede")

allan.pozdrav()


''''
allan.pozdrav()
allan.vydlisko()
allan.profesia()
allan.rod()
print(allan.farba_oci)
print(allan.vysku)
print(allan.edad)
allan.zostarnem(10)
print(f"so {allan.edad} starsi")'''


