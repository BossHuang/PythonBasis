__author__ = 'leihuang'

import module_51
import logging
try:
    weight = module_51.determine_weight(1, -1)
except module_51.InvalidDensityError:
    weight = 0
except module_51.Error as e:
    logging.error('Bug in the calling code: %s', e)
except Exception as e:
    logging.error('Bug in the API code: %s', e)
    raise