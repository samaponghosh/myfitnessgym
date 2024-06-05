import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear

def count():
    #stream = CamGear(source='https://192.168.238.76:8080/video', stream_mode = False, logging=True).start() # YouTube Video URL as input
    stream = CamGear(source=0).start()
#stream = cv2.VideoCapture("https://192.168.238.76:8080/")
#stream = CamGear(source="https://192.168.238.76:8080/").start()
    count=0
    while True:
        frame = stream.read()
        count += 1
        if count % 6 != 0:
            continue
 
        frame=cv2.resize(frame,(1020,600))
        bbox,label,conf = cv.detect_common_objects(frame)
        frame = draw_bbox(frame,bbox,label,conf)
        c = label.count('chair')
        cv2.putText(frame,str(c),(50,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
        cv2.imshow("FRAME",frame)
        if cv2.waitKey(1)&0xFF==27:
            break
    stream.release()
    cv2.destroyAllWindows()

#'https://www.youtube.com/watch?v=En_3pkxIJRM'
