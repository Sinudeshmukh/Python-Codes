class Student:

    school = 'SDSchool'

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    # decorator for calling class method
    @classmethod
    def school_info(cls):
        return cls.school

    @staticmethod
    def extra_info():
        return "static method is used when we don't want to use class or instance variable"


print(Student.school_info())

print(Student.extra_info())