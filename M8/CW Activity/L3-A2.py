class student:
    grade = 10
    name = "Penguin"

    #method1
    def introduction(self):
        print("Hi I am a student")

    #method2
    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()