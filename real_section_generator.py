import calendar
import random


class RealSection:
    def __init__(self, id, scheduled_section_id, real_arrival_time, train_id, event_id):
        self.id = id
        self.scheduled_section_id = scheduled_section_id
        self.real_arrival_time = real_arrival_time
        self.train_id = train_id
        self.event_id = event_id

    def __str__(self):
        return f"{self.id},{self.scheduled_section_id},{self.real_arrival_time},{self.train_id},{self.event_id}"


class RealSectionGenerator:
    def __init__(self, scheduled_sections, events, trains, year, amount_of_stations, amount_of_trains):
        self.scheduled_sections = scheduled_sections
        self.events = events
        self.trains = trains
        self.real_sections = []
        self.id = 0
        self.calendar_obj = calendar.Calendar()
        # generate calendar tuples for the year
        self.calendar_tuples = self.calendar_obj.yeardatescalendar(year, 12)
        # reshape calendar tuples to a list of dates
        self.dates = [
            date for month in self.calendar_tuples for week in month for day in week for date in day]
        # filter dates to contain only given year
        self.dates = list(filter(lambda date: date.year == year, self.dates))
        # remove duplicates from dates
        self.dates = list(dict.fromkeys(self.dates))
        self.amount_of_stations = amount_of_stations
        self.amount_of_trains = amount_of_trains

    def generate_real_sections(self):
        train_id = 0
        stations_covered = 0
        for date in self.dates:
            for scheduled_section in self.scheduled_sections:
                event = None
                if random.randint(1, 100000) == 1:
                    event = random.choice(self.events)
                if event is None:
                    real_section = RealSection(
                        self.id, scheduled_section.id, scheduled_section.arrival_time, train_id, None)
                else:
                    real_section = RealSection(
                        self.id, scheduled_section.id, scheduled_section.arrival_time, train_id, event.id)
                self.real_sections.append(real_section)
                self.id += 1
                stations_covered += 1
                if stations_covered == self.amount_of_stations - 1:
                    train_id += 1
                    stations_covered = 0
                    if train_id == self.amount_of_trains:
                        train_id = 0
                # print(real_section)

    def to_csv(self):
        with open('real_sections.csv', 'w') as file:
            file.write('id,scheduled_section_id,real_arrival_time,train_id,event_id\n')
            for section in self.real_sections:
                file.write(str(section) + '\n')
