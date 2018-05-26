__author__ = 'leihuang'

class Resistor(object):
    def __init__(self, ohms):
        print "Resistor"
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        print "VoltageResistance"
        super(VoltageResistance, self).__init__(ohms)
        #self._ohms = ohms
        #self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        print "1 ohms"
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        if hasattr(self, 'ohms'):
            raise ArithmeticError("can't set attritube of ohms")
        self._ohms = ohms


#v = VoltageResistance(-1)

v = VoltageResistance(5.0)


