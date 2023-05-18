class PassangerRide:
    def __init__(self, passanger_ride_id, entry_station_id, exit_station_id, entry_time):
        self.passanger_ride_id = passanger_ride_id
        self.entry_station_id = entry_station_id
        self.exit_station_id = exit_station_id
        self.entry_time = entry_time
        self.exit_time = None
        self.direction = 1 if entry_station_id < exit_station_id else -1
        self.train_id = None
        self.ride_id = None

    def exit_train(self, exit_time):
        self.exit_time = exit_time

    def board_train(self, train_id, ride_id, entry_time):
        self.train_id = train_id
        self.entry_time = entry_time
        self.ride_id = ride_id

    def __str__(self):
        return f"{self.passanger_ride_id},{self.entry_station_id},{self.exit_station_id},{self.entry_time},{self.exit_time},{self.train_id},{self.ride_id}"

    def to_csv(self, file_name, passanger_rides):
        with open(f'{file_name}', 'w', encoding='UTF-8') as file:
            for passanger_ride in passanger_rides:
                file.write(str(passanger_ride) + '\n')
