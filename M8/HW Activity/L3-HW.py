class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def introduce(self):
        print(f"Hello, I am {self.name}.")
        print(f"I am a {self.model} model, built in {self.year}.")
        print("Nice to meet you!\n")

robot1 = Robot("RoboMax", "XJ-9", 2023)
robot2 = Robot("AlphaBot", "Z-202", 2025)

robot1.introduce()
robot2.introduce()