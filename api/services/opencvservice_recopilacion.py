import cv2
import os
import imutils
import numpy as np
from pathlib import Path


def recopilacion(cod, nom):
    nombre = nom
    codigo_universitario = cod
    personName = "{}-{}".format(nombre, codigo_universitario)
    # Cambia a la ruta donde hayas almacenado Data
    dataPath = '{}/data'.format(Path.cwd())

    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0)  # cv2.CAP_DSHOW

    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:

        ret, frame = cap.read()
        if ret == False:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(frame, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count), rostro)
            count = count + 1
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        if count >= 300:
            break

    cap.release()
    # Esperara
    entrenandoRostro()


def entrenandoRostro():
    dataPath = '{}/data'.format(Path.cwd())
    peopleList = os.listdir(dataPath)

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        for fileName in os.listdir(personPath):
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName, 0))
            image = cv2.imread(personPath+'/'+fileName, 0)
        label = label + 1

    # Métodos para entrenar el reconocedor
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Entrenando el reconocedor de rostros
    face_recognizer.train(facesData, np.array(labels))

    # Almacenando el modelo obtenido
    face_recognizer.write('services/modeloEigenFace.xml')
    # face_recognizer.write('modeloFisherFace.xml')
    # face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo almacenado...")
