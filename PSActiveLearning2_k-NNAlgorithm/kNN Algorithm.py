import numpy as np
a = np.array((1,7))
b = np.array((3,7))

dist = np.sqrt(np.sum(np.square(a-b)))

print(dist)
