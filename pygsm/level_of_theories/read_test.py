import cclib
import sys
import numpy as np
import itertools

directory = sys.argv[1]
p = cclib.parser.Gaussian(directory)
data = p.parse()
energies = data.scfenergies
grads = data.grads
coords = data.atomcoords

print (energies)
print (grads)
print (coords)
