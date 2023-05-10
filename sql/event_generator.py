import numpy as np
from datetime import timedelta


class Event:
    def __init__(self, id, event_type, delay_amount):
        self.id = id
        self.event_type = event_type
        self.delay_amount = delay_amount

    def __str__(self):
        return f"{self.id},{self.event_type},{self.delay_amount}"


class EventGenerator:
    def __init__(self):
        self.events = []
        self.id = 0
        self.event_type = ""
        self.delay_amount = timedelta()

    def generate_events(self, num_events):
        for i in range(num_events):
            self.id = i
            event_type = ["delay", "breakdown", "accident"]
            self.event_type = np.random.choice(event_type)
            hours = np.random.randint(0, 24)
            minutes = np.random.randint(0, 60)
            seconds = np.random.randint(0, 60)
            self.delay_amount = timedelta(
                hours=hours, minutes=minutes, seconds=seconds)
            self.events.append(
                Event(self.id, self.event_type, self.delay_amount))

    def print_events(self):
        for event in self.events:
            print(f"{event.id},{event.event_type},{event.delay_amount}")

    def to_csv(self):
        with open("events.csv", "w") as file:
            file.write('id,event_type,delay_amount\n')
            for event in self.events:
                # print(str(event))
                file.write(str(event) + '\n')
