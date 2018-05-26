__author__ = 'leihuang'

class Resistor(object):
    def __init__(self, ohms):
        print "In Resistor"
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
        print "Out Resistor"

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        print "In VoltageResistance"
        super(VoltageResistance, self).__init__(ohms)
        print "Out VoltageResistance"

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        print "In ohms setter"
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        if hasattr(self, 'ohms'):
            raise ArithmeticError("can't set attritube of ohms")
        self._ohms = ohms
        print "Out ohms setter"

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms



#v = VoltageResistance(-1)

v = VoltageResistance(5.0)

#v.ohms = 3

print v.current
v.voltage = 2
print v.current


