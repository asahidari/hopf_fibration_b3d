"""
in init_pos s d=0.0 n=2
in final_pos s d=1.5708 n=2
in polar s d=1.5708 n=2
in division s d=10 n=2
out verts v
"""

import math
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList

p = init_pos
q = final_pos

verts = Vector3DList()
v = []
for i in range(division):
    r = 1.0
    az = p + (i/division) * (q - p)
    v.append(Vector((r*math.cos(az)*math.sin(polar), r*math.sin(az)*math.sin(polar), r*math.cos(polar))))
    # v.append((r, phi, theta))
verts.extend(v)