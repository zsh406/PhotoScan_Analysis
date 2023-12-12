import Metashape, math
import numpy as np # "C:\Program Files\Agisoft\Metashape Pro\python\python.exe" -m pip install numpy==1.13.3
# https://agisoft.freshdesk.com/support/solutions/articles/31000136860-how-to-install-external-python-module-to-metashape-professional-package

path = Metashape.app.getSaveFileName("Specify the export file path:", filter="Text file (*.txt);;All formats (*.*)")
file = open(path, "wt")
file.write("id\tX\tY\tZ\tv_x\tv_y\tv_z\tmaxEigenValue\n")

chunk = Metashape.app.document.chunk
T = chunk.transform.matrix
if chunk.transform.translation and chunk.transform.rotation and chunk.transform.scale:
    T = chunk.crs.localframe(T.mulp(chunk.region.center)) * T
R = T.rotation() * T.scale()

for point in chunk.tie_points.points:
    if not point.valid:
        continue
    cov = point.cov

    V = chunk.transform.matrix * point.coord
    V.size = 3
    X, Y, Z = chunk.crs.project(V)
    cov = R * cov * R.t()
    cov=np.asarray(cov).reshape(3,3)
    eigval, eigvec=np.linalg.eig(cov)
    index_max=np.argmax(eigval)
    vect=eigvec[:,index_max]
    val=np.sqrt(eigval[index_max])
    p1 = np.array([0, 0, 1])
    p2=vect

    angle = math.atan2(np.linalg.norm(np.cross(p1, p2)), p1.dot(p2.transpose()))
    if angle > math.pi / 2 or angle < -math.pi / 2:
        vect = -vect

    file.write(str(point.track_id))
    file.write("\t{:.6f}\t{:.6f}\t{:.6f}".format(X, Y, Z))
    file.write("\t{:.6f}\t{:.6f}\t{:.6f}".format(vect[0], vect[1], vect[2]))
    file.write("\t{:.6f}".format(val))
    file.write("\n")

file.close()

