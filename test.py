import math
import numpy as np
p1 = np.array([0, 0, 1])
p2=np.array([[-0.04793589, 0.45980732, 0.88672396]])
print(np.linalg.norm(np.cross(p1, p2)))
print(p1.dot( p2.transpose()))
angle = math.atan2(np.linalg.norm(np.cross(p1, p2)), p1.dot( p2.transpose()))
print(angle)