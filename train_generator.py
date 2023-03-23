import numpy as np
import random


class Trains:
    def __init__(self, id, standing_capacity, seating_capacity):
        self.id = id
        self.standing_capacity = standing_capacity
        self.seating_capacity = seating_capacity

    def __str__(self):
        return f"{self.id},{self.standing_capacity},{self.seating_capacity}"


class TrainGenerator:
    def __init__(self):
        self.trains = []
        self.id = 0
        self.standing_capacity = 0
        self.seating_capacity = 0

    def generate_trains(self, num_trains):
        for i in range(num_trains):
            self.id = i
            # generate random standing and seating capacity
            standing_capacity = random.randint(1100, 1300)
            seating_capacity = random.randint(220, 260)

            # create a new train with generated capacity
            train = Trains(self.id, standing_capacity, seating_capacity)
            self.trains.append(train)

    def print_trains(self):
        for train in self.trains:
            print(f"{train.id},{train.standing_capacity},{train.seating_capacity}")

    def to_csv(self):
        with open("trains.csv", "w") as file:
            file.write('id,standing_capacity,seating_capacity\n')
            for train in self.trains:
                file.write(str(train) + '\n')
