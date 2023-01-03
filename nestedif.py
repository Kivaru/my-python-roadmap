def switchExample(arg):
    switcher = {
        0: "This is zero",
        1: "This is one",
        2: "This is two"
    }

    return switcher.get(arg, "nothing")

print(switchExample(4))

