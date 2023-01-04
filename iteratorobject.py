class iteratedNumbers:
    #initialise object that return iterator itself
    def __iter__(self):
        self.a = 1
        return self

    #implements __next__ function which allows to do some operations
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = iteratedNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

    