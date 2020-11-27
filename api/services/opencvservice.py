import numpy as np
import cv2
import os
import imutils
from flask_restful import Resource
from flask import Response, request


class CapturandoRostros(Resource):

    def get(self):
        body = request.get_json()
        nombre = body['nombre']
        codigo_universitario = body['codigo_universitario']
        personName = "{}-{}".format(nombre, codigo_universitario)
        print(personName)
        dataPath = '/home/jeanpier/Documentos/project/IA/Project/api/data'
        personPath = dataPath + '/' + personName

        if not os.path.exists(personPath):
            print('Carpeta creada: ', personPath)
            os.makedirs(personPath)
        cap = cv2.VideoCapture(0)  # cv2.CAP_DSHOW  / cv2.CAP_V4L2
        # cap = cv2.VideoCapture(
        #     '/home/jeanpier/Documentos/project/IA/prueba/videos/SELF INTRODUCTION 1 MINUTE (how to introduce yourself).mp4')

        faceClassif = cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        count = 0
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()

            faces = faceClassif.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                rostro = auxFrame[y:y+h, x:x+w]
                rostro = cv2.resize(rostro, (150, 150),
                                    interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(
                    personPath + '/rotro_{}.jpg'.format(count), rostro)
                count = count + 1
            cv2.imshow('frame', frame)

            k = cv2.waitKey(27)
            if k == 233 or count >= 300:    # Esc key to stop
                break
            elif k == -1:  # normally -1 returned,so don't print it
                continue
            else:
                print(k)  # else print its value
            # if k == 27 or count >= 300:
            #     break
        cap.release()
        cv2.destroyAllWindows()

        entrenandoRostro()
        return "ok", 200


class entrenandoRostro(Resource):
    def __init__(self):

        # Cambia a la ruta donde hayas almacenado Data
        dataPath = '/home/jeanpier/Documentos/project/IA/Project/api/data'
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
        # print('labels= ',labels)
        # print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))

        # Métodos para entrenar el reconocedor
        face_recognizer = cv2.face.EigenFaceRecognizer_create()
        # face_recognizer = cv2.face.FisherFaceRecognizer_create()
        # face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Entrenando el reconocedor de rostros
        print("Entrenando...")
        face_recognizer.train(facesData, np.array(labels))

        # Almacenando el modelo obtenido
        face_recognizer.write('api/services/modeloEigenFace.xml')
        # face_recognizer.write('modeloFisherFace.xml')
        # face_recognizer.write('modeloLBPHFace.xml')
        print("Modelo almacenado...")


class reconocimientoFacial(Resource):
    def get(self):
        body = request.get_json()
        timeseconds = body['time']
        # Cambia a la ruta donde hayas almacenado Data
        dataPath = '/home/jeanpier/Documentos/project/IA/Project/api/data'
        imagePaths = os.listdir(dataPath)
        print('imagePaths=', imagePaths)

        face_recognizer = cv2.face.EigenFaceRecognizer_create()
        # face_recognizer = cv2.face.FisherFaceRecognizer_create()
        # face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Leyendo el modelo
        face_recognizer.read('api/services/modeloEigenFace.xml')
        # face_recognizer.read('modeloFisherFace.xml')
        # face_recognizer.read('modeloLBPHFace.xml')

        cap = cv2.VideoCapture(-1, cv2.CAP_V4L2)  # cv2.CAP_DSHOW
        # cap = cv2.VideoCapture(
        #     '/home/jeanpier/Documentos/project/IA/prueba/videos/SELF INTRODUCTION 1 MINUTE (how to introduce yourself).mp4')

        faceClassif = cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

        cv2.startWindowThread()
        # variables
        cpt = 0
        while True:
            ret, vista = cap.read()
            if ret == False:
                break
            gray = cv2.cvtColor(vista, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()

            faces = faceClassif.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                rostro = auxFrame[y:y+h, x:x+w]
                rostro = cv2.resize(rostro, (150, 150),
                                    interpolation=cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                cv2.putText(vista, '{}'.format(result), (x, y-5),
                            1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

                # EigenFaces
                if result[1] < 5700:
                    cv2.putText(vista, '{}'.format(
                        imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.rectangle(vista, (x, y), (x+w, y+h), (0, 255, 0), 2)
                else:
                    cv2.putText(vista, 'Desconocido', (x, y-20), 2,
                                0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(vista, (x, y), (x+w, y+h), (0, 0, 255), 2)
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

            cpt = cpt + 1
            cv2.namedWindow('vista')  # cv2.WINDOW_NORMAL)
            cv2.imshow('vista', vista)
            k = cv2.waitKey(27)
          #  print(cap.isOpened()) - no aprueba
            if k == 27 or cpt == timeseconds:
                break
        cap.release()
        cv2.destroyAllWindows()
        return "ok", 200
