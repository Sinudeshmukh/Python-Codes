class Student:

    school: 'SDSchool'

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def avg_cls(self):
        return (self.s1 + self.s2 + self.s3) / 3

    # Instance Method (Accessor/getters)

    def get_s1(self):
        return self.s1

    # Instance Method (Mutator/setters)

    def set_s1(self, value):
        self.s1 = value


cls1 = Student(1, 2, 3)
cls2 = Student(4, 5, 6)

print(cls1.avg_cls())

print(cls1.get_s1())

cls2.set_s1(3.5)

print(cls2.get_s1())
