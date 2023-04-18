class First:
    def display(self):
        print("First")


class Second():
    def display(self):
        print("second")


class Third(Second,First):  # left right taken first
                            #also whenever function called (which will it find first, it will execute)
    def display(self):
        print("third")


x = Third()
#x.display_third()
x.display()

print(Third.mro())
