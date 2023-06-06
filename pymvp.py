class Plant:
    def __init__(self, name, cost, growth_rate, sell_price):
        self.name = name
        self.cost = cost
        self.growth_rate = growth_rate
        self.sell_price = sell_price
        self.age = 0
        self.is_grown = False

    def grow(self):
        self.age += 1
        if self.age >= self.growth_rate:
            self.is_grown = True

    def sell(self):
        profit = self.sell_price - self.cost
        return profit

class Game:
    def __init__(self):
        self.plants = []
        self.money = 1000

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_plants(self):
        for plant in self.plants:
            plant.grow()

    def sell_plants(self):
        for plant in self.plants:
            if plant.is_grown:
                profit = plant.sell()
                self.money += profit
                self.plants.remove(plant)

    def play(self):
        while True:
            print("Your money:", self.money)
            for plant in self.plants:
                print(plant.name, plant.age, plant.is_grown)

            command = input("What would you like to do? (grow, sell, quit) ")
            if command == "grow":
                self.grow_plants()
            elif command == "sell":
                self.sell_plants()
            elif command == "quit":
                break

if __name__ == "__main__":
    game = Game()
    game.add_plant(Plant("Plant A", 10, 2, 150))
    game.add_plant(Plant("Plant B", 20, 3, 200))
    game.play()

