"""
in verts_in v d=[] n=1
in num s d=10 n=2
out verts_out v
out edges_out s
"""

import numpy as np
import math
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList, EdgeIndicesList

# total = len(verts_in)
# print(total)
verts_out = Vector3DList() # *total
edges_out = EdgeIndicesList() # *total

a, b, c = vert_in[0], vert_in[1], vert_in[2]
verts = []
edge_set = set()
if c >= 0.997:
    z_ = np.linspace(-1, 1, num)
    v = []
    for z in z_:
        v.append(Vector((0, 0, z)))
    verts = v
elif c == -1.:
    t_ = np.linspace(0, 2*math.pi, num)
    v = []
    for t in t_:
        v.append(Vector((0.5*math.cos(t), 0.5*math.sin(t), 0)))
    verts = v
else:
    alpha = math.sqrt(0.5 * (1 + c))
    beta = math.sqrt(0.5 * (1 - c))

    phi_ = np.linspace(0, 2*math.pi, num)
    v = []
    for phi in phi_:
        theta = math.atan2(a, b) - phi
        w, x, y, z = alpha * math.cos(theta), -1 * beta * math.cos(phi), -1 * beta * math.sin(phi), alpha * math.sin(theta)
        rr = math.acos(w) * (1./math.pi) * (1./math.sqrt(1-w**2))
        v.append(Vector((x*rr, y*rr, z*rr)))
    verts = v

verts_out.extend(verts)
        
for j in range(num-1):
    edge_set.add(tuple([j, j+1]))
if c < 0.997:
    edge_set.add(tuple([num-1, 0]))
edges_out.extend(list(edge_set))


