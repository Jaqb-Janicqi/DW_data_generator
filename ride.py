class Ride:
    def __init__(self, ride_id, train_id) -> None:
        self.ride_id = ride_id
        self.train_id = train_id

    def __str__(self) -> str:
        return f"{self.ride_id},{self.train_id}"