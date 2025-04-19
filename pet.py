class Pet:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age  # in years
        self.type = "Cat"
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.birthday = datetime.date.today().replace(year=datetime.date.today().year - age)

    def mood(self):
        if self.happiness >= 8:
            return "Excited"
        elif 5 <= self.happiness < 8:
            return "Okay"
        elif self.happiness < 5:
            return "Tired"

    def meow(self):
        return f"{self.name} says: Meow!"

    def respond(self):
        return f"{self.name} responds and smiles!"

    def feed(self, current_hour):
        if 6 <= current_hour <= 20:
            if self.hunger > 0:
                self.hunger -= 2
                if self.hunger < 0:
                    self.hunger = 0
                print(f"{self.name} has been fed.")
            else:
                print(f"{self.name} is already full!")
        else:
            print("It's not feeding time. Try between 6 AM and 8 PM.")

    def play(self):
        if self.energy > 2 and self.hunger < 9:
            self.happiness += 2
            self.energy -= 2
            self.hunger += 1
            if self.happiness > 10:
                self.happiness = 10
            print(f"{self.name} had fun playing!")
        else:
            print(f"{self.name} is too tired or hungry to play.")

    def sleep(self, current_hour):
        if 21 <= current_hour or current_hour < 6:
            if self.energy < 10:
                self.energy += 3
                if self.energy > 10:
                    self.energy = 10
                self.hunger += 1
                if self.hunger > 10:
                    self.hunger = 10
                print(f"{self.name} took a nap.")
            else:
                print(f"{self.name} is already fully rested.")
        else:
            print("It's not sleeping time. Cats usually sleep between 9 PM and 6 AM.")

    def check_health(self):
        if self.hunger >= 9 or self.energy <= 2:
            self.health -= 1
            if self.health < 0:
                self.health = 0
            print(f"{self.name} is not feeling well.")
        elif self.health < 10:
            self.health += 1  # recovers slowly if well cared for

    def __str__(self):
        return (f"{self.name} the {self.type} (Age: {self.age})\n"
                f"Hunger: {self.hunger}/10 | Energy: {self.energy}/10 | "
                f"Happiness: {self.happiness}/10 | Health: {self.health}/10\n"
                f"Mood: {self.mood()}")


            def eat(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(f"{self.name} eats and looks happy!")

    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10
        print(f"{self.name} curls up and takes a nap.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            if self.happiness > 10:
                self.happiness = 10
            self.hunger += 1
            if self.hunger > 10:
                self.hunger = 10
            print(f"{self.name} plays around excitedly!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        if not hasattr(self, 'tricks'):
            self.tricks = []
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if hasattr(self, 'tricks') and self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
