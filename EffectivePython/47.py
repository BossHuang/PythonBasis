__author__ = 'leihuang'

rate = 1.45
seconds = 3*60+42
cost = rate*seconds/60
print cost
print round(cost, 2)

rate = 0.05
seconds = 5
cost = rate*seconds/60
print cost
print round(cost, 2)

from decimal import Decimal,ROUND_UP
rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate*seconds/Decimal('60')
cost = cost.quantize(Decimal('0.01'), ROUND_UP)
print cost

rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate*seconds/Decimal('60')
cost = cost.quantize(Decimal('0.01'), ROUND_UP)
print cost