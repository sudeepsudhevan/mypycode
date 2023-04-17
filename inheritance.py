class Baseclass:
    def __init__(self):
        print("Base class")

    def set_name(self, name):
        self.name = name
        print("base class set name")


class Subclass(Baseclass):
    def __init__(self):  # constructor override (baseclass override by subclass)
        super().__init__()
        # Baseclass.__init__(self)

        print("Sub class")

    def set_name(self, name):
        self.name = name
        print("sub class set name")

    def welcome(self):
        print("welcome")

    def display_name(self):
        print("Name: " + self.name)


x = Subclass()
x.welcome()
x.set_name("Sudeep")
x.display_name()
