class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            print(f"Moving up from {self.current} to {self.current+1}")
            self.current += 1
            return True

        else:
            return False
    def floor_down(self):
        if self.current > self.bottom:
            print(f"Moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for n in range(floor - self.current):
                self.floor_up()
        elif floor < self.current:
            for n in range(self.current - floor):
                self.floor_down()
        else:
            print(f"We are currently on the floor {self.current}")
class Building:
    def __init__(self,bottom, top, elevators):
        self.elevators = []
        for n in range(elevators):
            self.elevators.append(Elevator(bottom,top))
    def run_elevator(self, elevator, floor):
        print(f"Moving elevator {elevator}:")
        self.elevators[elevator-1].go_to_floor(floor)
building=Building(1,8,4)
building.run_elevator(1,6)