import cv2
import os
import imutils
import numpy as np


def recopilacion(cod, nom):
    nombre = nom
    codigo_universitario = cod
    personName = "{}-{}".format(nombre, codigo_universitario)
    # Cambia a la ruta donde hayas almacenado Data
    dataPath = '/home/jeanpier/Documentos/project/IA/FaceRecognition/Live-Streaming-using-OpenCV-Flask/data'
    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        print('Carpeta creada: ', personPath)
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0)  # cv2.CAP_DSHOW
    # cap = cv2.VideoCapture(
    #     '/home/jeanpier/Documentos/project/IA/prueba/videos/SELF INTRODUCTION 1 MINUTE (how to introduce yourself).mp4')

    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:

        ret, frame = cap.read()
        if ret == False:
            break

        # img = np.frombuffer(frame, dtype=np.uint8).reshape((300, 300, 4))
        # print(img.shape)
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

        k = cv2.waitKey(1)
        if k == 27 or count >= 300:
            break

    cap.release()
    cv2.destroyAllWindows()
    # Esperara
    entrenandoRostro()


def entrenandoRostro():
    dataPath = '/home/jeanpier/Documentos/project/IA/FaceRecognition/Live-Streaming-using-OpenCV-Flask/data'
    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')

        for fileName in os.listdir(personPath):
            print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName, 0))
            image = cv2.imread(personPath+'/'+fileName, 0)
            # cv2.imshow('image',image)
            # cv2.waitKey(10)
        label = label + 1
    # cv2.destroyAllWindows
    #print('labels= ',labels)
    #print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))

    # Métodos para entrenar el reconocedor
    print(dir(cv2.face))
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Entrenando el reconocedor de rostros
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    # Almacenando el modelo obtenido
    face_recognizer.write('api/services/modeloEigenFace.xml')
    # face_recognizer.write('modeloFisherFace.xml')
    # face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo almacenado...")
