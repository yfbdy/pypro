a = 5
b = 10


def add(a, b):
    return a + b


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("self ", self)

    def show(ss):
        print(ss.name, ss.age)
        print("ss", ss)

print('__name__ :',__name__)

if __name__ == '__main__':
    person = Person('xx',18)
    print("对象内存地址 ",id(person),"对象类型：",type(person))
    person.show();