import calendar
import random
from datetime import datetime, timedelta
import csv


class RealSection:
    def __init__(self, RealSectionId, TrainId, TimeId, DateId, EventId, StartStationId, EndStationId, AmountOfPassengers, DelayAmount, ArrivalTime, RealArrivalTime):
        self.RealSectionId = RealSectionId
        self.TrainId = TrainId
        self.TimeId = TimeId
        self.DateId = DateId
        self.EventId = EventId
        self.StartStationId = StartStationId
        self.EndStationId = EndStationId
        self.AmountOfPassengers = AmountOfPassengers
        self.DelayAmount = DelayAmount
        self.ArrivalTime = ArrivalTime
        self.RealArrivalTime = RealArrivalTime

    def __str__(self):
        return f"{self.RealSectionId},{self.TrainId},{self.TimeId},{self.DateId},{self.EventId},{self.StartStationId},{self.EndStationId},{self.AmountOfPassengers},{self.DelayAmount},{self.ArrivalTime},{self.RealArrivalTime}"



class RealSectionGenerator:
    def __init__(self, scheduled_sections, trains, year, amount_of_stations, amount_of_trains, dates_objects, times, passenger_gen):
        self.scheduled_sections = scheduled_sections
        self.trains = trains
        self.real_sections = []
        self.id = 0
        self.times = times

        self.calendar_obj = calendar.Calendar()
        self.calendar_tuples = self.calendar_obj.yeardatescalendar(year, 12)
        # reshape calendar tuples to a list of dates
        self.dates = [
            date for month in self.calendar_tuples for week in month for day in week for date in day]
        # filter dates to contain only given year
        self.dates = list(filter(lambda date: date.year == year, self.dates))
        # remove duplicates from dates
        self.dates = list(dict.fromkeys(self.dates))

        self.dates_objects = dates_objects
        self.amount_of_stations = amount_of_stations
        self.amount_of_trains = amount_of_trains
        self.passenger_gen = passenger_gen

    def generate_real_sections(self):
        files_generated = 0
        train_id = 0
        stations_covered = 0
        date_num = 0
        last_arrival_time = None
        sections_generated = 0
        # extract days from dates
        # months = []
        # january = [date for date in self.dates if date.month == 1]
        # february = [date for date in self.dates if date.month == 2]
        # months = [january, february]
        # get first two dates 
        days = [date for date in self.dates if date.month == 1][:2]
        for date in days:
            for scheduled_section in self.scheduled_sections:

                # if scheduled_section.arrival_time.hour == 12 and last_arrival_time.hour == 11:
                #     self.to_csv(f"real_sections_{date_num}.csv")
                #     files_generated += 1
                #     self.real_sections = []

                last_arrival_time = scheduled_section.arrival_time
                if last_arrival_time > scheduled_section.arrival_time:
                    date_num += 1

                event_id = 0
                if random.randint(1, 10000) == 1:
                    event_id = random.randrange(-1, 52)

                year = date.year
                month = date.month
                day = date.day
                # get date_id from dates that has the same year, month and day as the scheduled_section
                date_id = next((date.Id for date in self.dates_objects if date.year == year and date.month == month and date.day == day), None)

                # get time_id from times that has the same hour and minute as the scheduled_section
                time_id = next((time.Id for time in self.times if time.hour == scheduled_section.arrival_time.hour and time.minute == scheduled_section.arrival_time.minute), None)

                StartStationId = scheduled_section.start_station_id
                EndStationId = scheduled_section.end_station_id

                # get amount of passengers
                amount_of_passangers = self.passenger_gen.get_number_of_passangers(
                    self.dates_objects[date_num], self.times[time_id])

                if random.randint(1, 10) == 1:
                    DelayAmount = random.randrange(1, 3)
                else:
                    DelayAmount = 0

                date_FREEVARIABLENAME = self.dates_objects[date_num]
                time_FREEVARIABLENAME = scheduled_section.arrival_time
                ArrivalTime = datetime(date_FREEVARIABLENAME.year, date_FREEVARIABLENAME.month, date_FREEVARIABLENAME.day, time_FREEVARIABLENAME.hour, time_FREEVARIABLENAME.minute)
                RealArrivalTime = ArrivalTime + timedelta(minutes=DelayAmount)
                
                real_section = RealSection(self.id, train_id, time_id, date_id, event_id, StartStationId, EndStationId,
                                            amount_of_passangers, DelayAmount, ArrivalTime, RealArrivalTime)
                self.real_sections.append(real_section)
                self.id += 1
                stations_covered += 1
                sections_generated += 1
                if sections_generated == 10:
                    self.to_csv(f"real_sections_{files_generated}.csv")
                    self.real_sections = []
                    files_generated += 1
                if sections_generated == 20:
                    self.to_csv(f"real_sections_{files_generated}.csv")
                    return
                if stations_covered == self.amount_of_stations - 1:
                    train_id += 1
                    stations_covered = 0
                    if train_id == self.amount_of_trains:
                        train_id = 0
            
            self.to_csv(f"real_sections_{files_generated}.csv")
            files_generated += 1
            # print(real_section)
        # self.to_csv(f"real_sections_{date_num}.csv")

    def to_csv(self, filename):
        num = 0
        with open(filename, 'w', newline='', encoding= "utf-8") as file:
            for real_section in self.real_sections:
                if num != 0:
                    file.write('\n')
                num += 1
                file.write(real_section)
