# Import driver error base class
from device.utilities.exceptions import ExceptionLogger


class DriverError(ExceptionLogger):
    pass


class InitError(DriverError):
    message_base = "Unable to initialize"


class SetupError(DriverError):
    message_base = "Unable to setup"


class SetRgbError(DriverError):
    message_base = "Unable to set rgb"
