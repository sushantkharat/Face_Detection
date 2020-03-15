import cv2
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def draw_line(n,width=3,color=(255,0,255)):
    x1 = landmarks.part(n).x
    y1 = landmarks.part(n).y
    x2 = landmarks.part(n+1).x
    y2 = landmarks.part(n+1).y
    cv2.line(frame,(x1,y1),(x2,y2),color,width)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        ##For rectangle...
        # left = face.left()
        # right = face.right()
        # top = face.top()
        # bottom = face.bottom()
        # cv2.rectangle(frame,(left,top),(right,bottom),(255,255,0),3)

        landmarks = predictor(gray, face)

        for n in range(0, 68):
            ##To Draw points...
            # x = landmarks.part(n).x
            # y = landmarks.part(n).y
            # cv2.circle(frame, (x, y), 3, (0,0, 255), -1)
            
            ##To Draw lines...
            if n<16:
                draw_line(n,2)        #for jaw_line
            if n>=17 and n<=20:
                draw_line(n,2)         #for left_eyebrow
            if n>=22 and n<=25:
                draw_line(n,2)         #for right_eyebrow
                
            if n>=27 and n<=34:       
                draw_line(n,2)          #for nose
            if n>=36 and n<=40:
                draw_line(n,2)          #for left_eye
            if n>=42 and n<=46:
                draw_line(n,2)          #for right_eye

            if n>=48 and n<=58:
                draw_line(n,2)          #for mouth (outer)
            if n>=60 and n<67:
                draw_line(n,2)          #for mouth (inner)
            
    cv2.imshow("Output Frame",frame)

    key = cv2.waitKey(1)

    if key == 27 or key == ord('q'):
        break