import numpy as np
import datetime
from real_section import RealSection


class Train:
    def __init__(self, Trainid, standing_capacity, seating_capacity, section_times):
        self.Trainid = Trainid
        self.standing_capacity = standing_capacity
        self.seating_capacity = seating_capacity
        self.passangers = []
        self.section_times = section_times
        self.direction = None  # 1 for forward, -1 for backward, None for not started
        self.is_free = True
        self.current_station = None
        self.end_station = None
        self.scheduled_sections = None
        self.ride_id = None
        self.current_time = None

    def start_ride(self, start_station, ride_id, direction, current_time, scheduled_sections):
        self.current_station = start_station
        self.current_time = current_time
        self.direction = direction
        self.is_free = False
        self.end_station = len(self.section_times) - \
            1 if self.direction == 1 else 0
        self.ride_id = ride_id
        self.scheduled_sections = scheduled_sections

    def board_passangers(self, metro_line):
        for passanger in metro_line[self.current_station]:
            if passanger.direction == self.direction:
                passanger.board_train(self.Trainid, self.ride_id, self.current_time)
                self.passangers.append(passanger)
                metro_line[self.current_station].remove(passanger)


    def unboard_passangers(self, passanger_rides):
        for passanger in self.passangers:
            if passanger.exit_station_id == self.current_station:
                passanger.exit_train(self.current_time)
                passanger_rides.append(passanger)
                self.passangers.remove(passanger)
        

    def next_station(self, metro_line, real_section_id, passanger_rides):
        self.unboard_passangers(passanger_rides)
        self.board_passangers(metro_line)
        if self.direction == 1:
            if self.current_station < len(self.section_times):
                self.current_station += 1
        else:
            if self.current_station > 0:
                self.current_station -= 1
        if self.current_station == self.end_station:
            for passanger in self.passangers:
                passanger.exit_train(self)
                self.passangers.remove(passanger)
            self.is_free = True
        self.current_time += datetime.timedelta(minutes=self.section_times[self.current_station])
        # random chance of delay caused by event
        event_id = ''
        if np.random.randint(0, 100) < 1:
            self.current_time += datetime.timedelta(minutes=1)
            event_id = np.random.randint(1, 53)
        return RealSection(
            real_section_id,
            self.scheduled_sections[self.current_station],
            self.current_time,
            self.Trainid,
            event_id,
            self.ride_id)
    
    def is_on_station(self, global_time):
        return global_time == self.current_time

    def __str__(self):
        return f"{self.Trainid},{self.standing_capacity},{self.seating_capacity}"


class TrainGenerator:
    def __init__(self, num_trains, section_times):
        self.trains = []
        self.free_trains = []
        self.section_times = section_times
        self.train_amount = 0
        self.generate_trains(num_trains)

    def generate_trains(self, num_trains, standing_capacity=1000, seating_capacity=200):
        for _ in range(num_trains):
            train = Train(self.train_amount, standing_capacity,
                          seating_capacity, self.section_times)
            self.train_amount += 1
            self.free_trains.append(train)

    def get_free_train(self):
        if len(self.free_trains) <= 0:
            self.generate_trains(1, 1200, 400)
        self.trains.append(self.free_trains.pop())
        return self.trains[-1]
    
    def free_train(self, train):
        self.free_trains.append(train)
        self.trains.remove(train)

    def print_trains(self):
        for train in self.trains:
            print(
                f"{train.Trainid},{train.standing_capacity},{train.seating_capacity}")

    def update_trains(self):
        for train in self.trains:
            train.seating_capacity = 400
            train.standing_capacity = 1200
        for train in self.free_trains:
            train.seating_capacity = 400
            train.standing_capacity = 1200

    def to_csv(self, file_name):
        with open(f'{file_name}', "w", encoding='UTF-8') as file:
            for train in self.trains:
                file.write(str(train) + '\n')
