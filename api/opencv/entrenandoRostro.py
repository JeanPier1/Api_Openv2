import cv2
import os
import numpy as np

# Cambia a la ruta donde hayas almacenado Data
dataPath = '/home/jeanpier/Documentos/project/IA/prueba/datav2'
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
face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
face_recognizer.write('modelov2EigenFace.xml')
# face_recognizer.write('modeloFisherFace.xml')
# face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado...")

# pip uninstall opencv_contrib_python
# and install again
# pip install opencv_contrib_python
#
