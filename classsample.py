class MysampleClass:
    def hello(self, n):
        self.name = n

    def print_name(self):
        print(self.name)


x = MysampleClass()
y = MysampleClass()
name = "sudeep"

x.hello(name)
y.hello("remanan")
# MysampleClass.hello(x)

x.print_name()
y.print_name()
