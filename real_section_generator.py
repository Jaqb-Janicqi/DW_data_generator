import calendar


class RealSection:
    def __init__(self, id, scheduled_section_id, real_arrival_time, train_id):
        self.id = id
        self.scheduled_section_id = scheduled_section_id
        self.real_arrival_time = real_arrival_time
        self.train_id = train_id


class RealSectionGenerator:
    def __init__(self, scheduled_sections, events, trains, year):
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

    def generate_real_sections(self):
        for scheduled_section in self.scheduled_sections:
            real_section = RealSection(
                self.id, scheduled_section.id, scheduled_section.arrival_time, 0)
