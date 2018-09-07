__author__ = 'leihuang'

class Error(Exception):
    """
    Base-class for all exceptions raised by this moule.
    """

class InvalidDensityError(Exception):
    """
    There was a problem with a provided density value.
    """

def determine_weight(volume, density):
    """
    calculate weight by volume and density
    :param volume:
    :param density:
    :return:weight
    """
    if density <= 0:
        raise InvalidDensityError
    return volume*density

class WeightError(Error):
    """
    Base-class for weight calculation errors
    """
class VolumeError(Error):
    """
    Base-class for volume calculation errors
    """
class DensityError(Error):
    """
    Base-class for density calculation errors
    """
