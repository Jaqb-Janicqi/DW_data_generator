class RealSection:
    def __init__(self, real_section_id, scheduled_section_id, real_arrival_time, train_id, event_id, ride_id) -> None:
        self.real_section_id = real_section_id
        self.scheduled_section_id = scheduled_section_id
        self.real_arrival_time = real_arrival_time
        self.train_id = train_id
        self.event_id = event_id
        self.ride_id = ride_id

    def __str__(self) -> str:
        return f"{self.real_section_id},{self.scheduled_section_id},{self.real_arrival_time},{self.train_id},{self.event_id},{self.ride_id}"
    
    def to_csv(self, file_name, sections):
        with open(f'{file_name}', 'w', encoding='UTF-8') as file:
            for section in sections:
                file.write(str(section) + '\n')