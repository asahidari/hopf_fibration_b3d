"""
in init_pos v d=(1,0,1.570796) n=2
in final_pos v d=(1,0,0) n=2
in division s d=10 n=2
out verts v
"""

import math
import numpy as np
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList

verts = Vector3DList()
v = []
p = np.array([init_pos[0]*math.cos(init_pos[1])*math.sin(init_pos[2]), init_pos[0]*math.sin(init_pos[1])*math.sin(init_pos[2]), init_pos[0]*math.cos(init_pos[2])])
q = np.array([final_pos[0]*math.cos(final_pos[1])*math.sin(final_pos[2]), final_pos[0]*math.sin(final_pos[1])*math.sin(final_pos[2]), final_pos[0]*math.cos(final_pos[2])])

a = np.dot(p, q)
w = q - a*p
q_prime = w/np.linalg.norm(w)
alpha = 2*math.pi

for i in range(division):
    alpha_i = alpha*i/division
    v_np = p*math.cos(alpha_i)+q_prime*math.sin(alpha_i)
    v.append(Vector((v_np[0], v_np[1], v_np[2])))
    # v.append((r, phi, theta))
verts.extend(v)