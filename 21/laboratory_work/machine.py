class Machine:
    is_on = False

    def turn_on(self):
        if self.is_on:
            print("Machine's already on")
        else:
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            self.is_on = False
        else:
            print("Machine's already off")


class HomeAppliance(Machine):
    is_pluged = False

    def plug_in(self):
        if self.is_pluged:
            print("Machine's already pluged in")
        else:
            self.is_pluged = True

    def plug_off(self):
        if self.is_pluged:
            self.is_pluged = False
        else:
            print("Machine's already unpluged")


class WashingMachine(HomeAppliance):
    def run(self):
        if self.is_pluged and self.is_on:
            print("Washing")
        else:
            print("Plug in or turn on the machine")


class LightSource(HomeAppliance):
    light_level = 100

    def set_level(self, level):
        if level < 1 or level > 100:
            print("Impossible level of light")
        else:
            self.light_level = level


class AutoVehicle(Machine):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y


class Car(AutoVehicle):
    def __init__(self, x=0, y=0, speed=10):
        super().__init__(x, y)
        self.speed = speed

    def set_speed(self, speed):
        if speed < 1:
            print("Car won't move")
        else:
            self.speed = speed

    def run(self, x, y):
        if not self.is_on:
            print("Need to turn on car first")
        else:
            print("The car is moving")
            while self.x != x or self.y != y:
                print(f"position x: {self.x}, y: {self.y}")
                self.x += self.speed
                self.y += self.speed
                if self.x > x:
                    self.x = x
                if self.y > y:
                    self.y = y
                if self.x == x and self.y == y:
                    print(f"position x: {self.x}, y: {self.y}")
                    break


bosch = WashingMachine()
bosch.plug_in()
bosch.turn_on()
bosch.run()
light_bulb = LightSource()
light_bulb.plug_in()
light_bulb.set_level(60)
light_bulb.turn_on()
print(light_bulb.light_level)

honda = Car()
honda.set_position(30, 40)
honda.turn_off()
honda.set_speed(60)
honda.run(180, 240)
