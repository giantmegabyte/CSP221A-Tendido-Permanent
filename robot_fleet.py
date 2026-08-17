import abc
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

#1.4
class InsufficientBatteryError(Exception):
    def __init__(self, robot_name, required, available):
        self.robot_name = robot_name
        self.required = required
        self.available = available
        message = (
            f"{robot_name} needs {required}% battery for this task "
            f"but only has {available}%."
        )
        super().__init__(message)

#1.1
class Robot(abc.ABC):
    #base class tanan nga robot

    manufacturer = "robobo inc."
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self._battery = 0
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    
    def battery(self, value):
        self._battery = max(0, min(100, value))

    def use_battery(self, amount):
        
        if amount > self._battery:
            raise InsufficientBatteryError(self.name, amount, self._battery)
        self.battery -= amount 

    @abc.abstractmethod
    def perform_task(self, **kwargs):
        raise NotImplementedError

    @classmethod
    def from_config(cls, config):
        return cls(**config)

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, battery={self.battery!r})"

#1.2
class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity

    def perform_task(self, **kwargs):
        cost = 10
        self.use_battery(cost)
        return f"{self.name} vacuumed the living room (used {cost}% battery)."

class DroneRobot(Robot):
    def __init__(self, name, battery=100, max_altitude=120):
        super().__init__(name, battery)
        self.max_altitude = max_altitude

    def perform_task(self, **kwargs):
        cost = 25
        self.use_battery(cost)
        return f"{self.name} completed an aerial survey (used {cost}% battery)."


#1.3
def fleet_report(robots):
    print("\n--- Fleet Status Report ---")
    for robot in robots:
        print(f"  {str(robot)}")
    print("---------------------------\n")

#1.5
def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as e:
        logging.error(str(e))
    else:
        print(f"Task result: {result}")
    finally:
        print(f"Current battery for {robot.name}: {robot.battery}%\n")

#-test
if __name__ == "__main__":
    r = CleaningRobot("Roomba")
    d = DroneRobot.from_config({"name": "Aqua-Drone", "battery": 15})
    fleet_report([r, d])
    run_task_safely(r)
    run_task_safely(d) 