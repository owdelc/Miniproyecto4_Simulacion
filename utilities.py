'''

UNIVERSIDAD DEL VALLE DE GUATEMALA
MODELACION Y SIMULACION
MIRKA MONZON 18139
OSCAR DE LEON 19298
ANDRES QUINTO 18288

MINIPROYECTO 4 - SIMULACION SERVIDORES

'''

import numpy as np
import random
import math


def exponential_random(lambda_max):
    return -(1/lambda_max)*(np.log(np.random.uniform()))