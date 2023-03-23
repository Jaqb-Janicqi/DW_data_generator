import pandas as pd
import calendar
import datetime


class ScheduledSection():
    def __init__(self, section_id, start_station_id, end_station_id, arrival_time):
        self.id = section_id
        self.start_station_id = start_station_id
        self.end_station_id = end_station_id
        self.arrival_time = arrival_time

    def __str__(self):
        return f"{self.id},{self.start_station_id},{self.end_station_id},{self.arrival_time}"


class ScheduledSectionGenerator():
    def __init__(self, year, timetable):
        self.timetable = timetable
        self.scheduled_sections = []
        self.year = year
        self.calendar_obj = calendar.Calendar()
        # generate calendar tuples for the year
        self.calendar_tuples = self.calendar_obj.yeardatescalendar(year, 12)
        # reshape calendar tuples to a list of dates
        self.dates = [
            date for month in self.calendar_tuples for week in month for day in week for date in day]

    def generate_scheduled_sections(self):
        id = 0
        for i in range(len(self.timetable)):
            for j in range(len(self.timetable[i])):
                for k in range(len(self.timetable[i][j])):
                    # if self.timetable[i][j][k] is not of type datetime.time, convert it to datetime.time
                    if not isinstance(self.timetable[i][j][k], datetime.time):
                        self.timetable[i][j][k] = self.timetable[i][j][k].time()
                    if i % 2 == 0:
                        self.scheduled_sections.append(
                            ScheduledSection(id, k, k+1, self.timetable[i][j][k]))
                    else:
                        entry = len(self.timetable[i][j]) - k
                        exit = len(self.timetable[i][j]) - k - 1
                        self.scheduled_sections.append(ScheduledSection(
                            id, entry, exit, self.timetable[i][j][k]))
                        print(self.scheduled_sections[-1])
                    id += 1

    def to_csv(self):
        with open('scheduled_sections.csv', 'w') as file:
            file.write('id,start_station_id,end_station_id,arrival_time\n')
            for section in self.scheduled_sections:
                file.write(str(section) + '\n')
