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
    def __init__(self, simulation_start_time, simulation_end_time, timetables):
        self.simulation_start_time = simulation_start_time
        self.simulation_end_time = simulation_end_time
        self.timetables = timetables
        self.scheduled_sections = []

    def generate_scheduled_sections(self):
        section_id = 0
        stations_count = len(self.timetables[0][0])
        current_time = self.simulation_start_time
        files_generated = 0

        timetable_index = -1
        for timetable in self.timetables:
            timetable_index += 1
            while current_time < self.simulation_end_time:
                stations_covered = 0
                for i in range(len(timetable)):
                    for section_time in timetable[i]:
                        if not isinstance(section_time, datetime.time):
                            break
                        current_time = datetime.datetime.combine(current_time.date(), section_time)
                        if timetable_index == 0:
                            self.scheduled_sections.append(
                                ScheduledSection(section_id, stations_covered,
                                                stations_covered + 1, current_time))
                        else:
                            self.scheduled_sections.append(
                                ScheduledSection(section_id, stations_count - stations_covered,
                                                stations_count - stations_covered - 1, current_time))
                        section_id += 1
                        stations_covered += 1
                    stations_covered = 0
                current_time += datetime.timedelta(days=1)
            current_time = self.simulation_start_time
        # self.to_csv(f"scheduled_sections{files_generated}.csv")
        return self.scheduled_sections

    def to_csv(self, file_name, sections):
        with open(f'{file_name}', 'w', encoding='UTF-8') as file:
            for section in sections:
                file.write(str(section) + '\n')
