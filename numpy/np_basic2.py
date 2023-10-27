#!/usr/bin/env python3

import numpy as np

#con isfinite se comprueba cada valor diciendote si es infinito o no

# np. nan sirve para representa un valor nulo y np.inf representa un valor infinito

x = np.array([1, 2, np.nan, np.inf])
print(np.isfinite(x))

