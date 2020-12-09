from flask import Flask, render_template, Response, request
import cv2
import os
import numpy as np


def Recursos(cod, nom):
    camera = cv2.VideoCapture(0)
    cpt = 0
    while True:
        # Capture frame-by-frame}
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            k = cv2.waitKey(1)
            cpt = cpt+1
            if k == ord("q") or cpt == 1000:
                break

# -----------------
# -----------------


def reconocimientofc(tiempo):

    timeseconds = tiempo
    dataPath = '/home/jeanpier/Documentos/project/IA/FaceRecognition/Live-Streaming-using-OpenCV-Flask/data'

    imagePaths = os.listdir(dataPath)
    print('imagePaths=', imagePaths)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Leyendo el modelo
    face_recognizer.read('api/services/modeloEigenFace.xml')
    # face_recognizer.read('modeloFisherFace.xml')
    # face_recognizer.read('modeloLBPHFace.xml')

    cap = cv2.VideoCapture(0)  # cv2.CAP_DSHOW
    # cap = cv2.VideoCapture(
    #     '/home/jeanpier/Documentos/project/IA/prueba/videos/SELF INTRODUCTION 1 MINUTE (how to introduce yourself).mp4')
    cpt = 0
    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            cv2.putText(frame, '{}'.format(result), (x, y-5),
                        1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            # EigenFaces
            if result[1] < 5700:
                cv2.putText(frame, '{}'.format(
                    imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'Desconocido', (x, y-20), 2,
                            0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            '''
            # FisherFace
            if result[1] < 500:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            '''
            # LBPHFace
            # if result[1] < 70:
            # 	cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            # 	cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            # else:
            # 	cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            # 	cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        k = cv2.waitKey(1)
        cpt = cpt+1
        if k == ord("q") or cpt == timeseconds:
            break
    cap.release()
    cv2.destroyAllWindows()
