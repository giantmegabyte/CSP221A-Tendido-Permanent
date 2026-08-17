import abc


class Robot(abc.ABC):
    """Abstract base class for all robots in the fleet."""

    manufacturer = "RoboCorp Industries"
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

    @abc.abstractmethod
    def perform_task(self, **kwargs):
        """Every subclass must implement its own task behavior."""
        raise NotImplementedError

    @classmethod
    def from_config(cls, config):
        """Alternative constructor: build a robot from a dict."""
        return cls(**config)

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, battery={self.battery!r})"