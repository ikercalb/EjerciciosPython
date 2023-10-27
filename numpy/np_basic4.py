#!/usr/bin/env python3

import numpy as np

#con equal se compara exactamente el las arrays que se le pasen
#all close es como equal pero sin tolerancia alguan

a = np.array([2, 3, 5, np.inf, np.nan])
b = np.array([2, 3, 5, np.inf, np.nan])

print(np.equal(a, b))
print(np.allclose(a,b))
