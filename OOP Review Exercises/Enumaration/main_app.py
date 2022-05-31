from enum import Enum


class GenericException(Exception):
    pass


class Timeout(Exception):
    pass


class AppException(Enum):
    pass
