from abc import ABC, abstractmethod


class Airplane(ABC):
    pass


class FlightSimulator(Airplane):
    speed = ''
    altitude = ''
    roll_angle = ''
    pitch_angle = ''
    yaw_angle = ''

    def fly(self):
        print('fly')


class FlightBooking(Airplane):
    seats = []

    def reserve_seat(self, n):
        print('booking: %s' % n)


if __name__ == '__main__':
    '''trừu tượng'''
    simulator = FlightSimulator()
    simulator.fly()
    booking = FlightBooking()
    seat_index = 1
    booking.reserve_seat(n=seat_index)

