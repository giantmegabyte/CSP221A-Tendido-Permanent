import abc

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