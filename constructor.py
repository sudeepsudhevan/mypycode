class SampleClass:
    year = 2020 # class variable

    def __init__(self, name, age, place): # object nte variable
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("year: "+str(SampleClass.year))
        print("Name : " + self.name)
        print("Age : " + str(self.age))
        print("palce : " + self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1


x = SampleClass("Sudeep", 24, "Achankunnu")
y = SampleClass("Remnaa", 26, "Thrissur")

x.display()
y.display()

SampleClass.year = SampleClass.year + 1
x.add_age()
y.add_age()
print("-----------------------------------------------------------------------")
x.display()
y.display()

print("-----------------------------------------------------------------------")
SampleClass.add_year()
x.add_age()
y.add_age()

x.relocate("mumbai")
y.relocate("pandora")
x.display()
y.display()