"""
in init_pos v d=(1,0,1.570796) n=2
in final_pos v d=(1,3.141592,0) n=2
in division s d=32 n=2
out verts v
"""

import math
import numpy as np
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList

verts = Vector3DList()
v = []

t_ = np.linspace(0.0, 1.0, division)
az_start = init_pos[1]
po_start = init_pos[2]
az_end = final_pos[1]
po_end = final_pos[2]


for t in t_:
    az_t = (1-t)*az_start + t*az_end
    po_t = (1-t)*po_start + t*po_end
    v.append(Vector((math.cos(az_t)*math.sin(po_t), math.sin(az_t)*math.sin(po_t), math.cos(po_t))))
verts.extend(v)