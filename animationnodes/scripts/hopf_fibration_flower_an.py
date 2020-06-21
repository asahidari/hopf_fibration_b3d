"""
in N s d=4 n=2
in A s d=0.5 n=2
in B s d=0.44880 n=2
in P s d=1.570796 n=2
in Q s d=0.0 n=2
in division s d=32 n=2
out verts v
"""

# N = 4 #controls the number of petals
# A = .5 #controls the fattness of the petals
# B = -pi/7 #controls the amplitude of the polar angle range
# P = pi/2 #controls the latitude of the flower
# Q = 0 #shifts the azmuthal angle

import math
import numpy as np
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList

verts = Vector3DList()
v = []

t_ = np.linspace(0.0, 1.0, division)

for t in t_:
    az_t = (2*math.pi)*t + A*math.cos(N*(2*math.pi)*t) + Q
    po_t = B*math.sin(N*(2*math.pi)*t) + P
    v.append(Vector((math.cos(az_t)*math.sin(po_t), math.sin(az_t)*math.sin(po_t), math.cos(po_t))))
verts.extend(v)