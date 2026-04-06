class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi phải >= 0")
        self._age = age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"

    def greet(self):
        return f"Hello, I am {self._name}"

    @classmethod
    def species(cls):
        return "Human"

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._name == other._name and self._age == other._age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        if grade < 0 or grade > 10:
            raise ValueError("Điểm không hợp lệ")
        self._grade = grade

    def __str__(self):
        return super().__str__() + f", Grade: {self._grade}"

    def study(self):
        return "Studying..."


def bai9():
    p = Person("An", 20)
    s = Student("Binh", 18, 8)

    print(p)
    print(p.greet())
    print(Person.species())
    print(Person.is_adult(20))

    print(s)
    print(s.study())

    print("So sánh:", p == Person("An", 20))

