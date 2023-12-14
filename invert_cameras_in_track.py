import Metashape, math
import numpy as np

LABEL_FOR_EXPORT = "Roundtrip"

chunk = Metashape.app.document.chunk
T = chunk.transform.matrix
print(T)
cameraTracks = chunk.camera_tracks
for track in cameraTracks:    
    if track.label == LABEL_FOR_EXPORT:
        
        for camera in track.keyframes:
            
            # cam_T = T * camera.transform
            # # R = camera.reference.rotation
            # # camera.reference.rotation = R.inv()
            # R = cam_T.rotation()
            # print(R)


            R = camera.transform.rotation()           
            # R = R.inv()
            C = camera.transform.translation()
            # C = Metashape.Vector((0,0,0))
            T2 = Metashape.Matrix([[R[0, 0], R[0, 1], R[0, 2], C[0]],
                          [R[1, 0], R[1, 1], R[1, 2], C[1]],
                          [-R[2, 0], -R[2, 1], -R[2, 2], C[2]],
                          [      0,       0,       0,    1]])
            camera.transform = T2
            # camera.transform = T2*camera.transform




print("Script finished!")

