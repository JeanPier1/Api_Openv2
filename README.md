# PROJECTO Eduvi

Creditos a Edson , Abdiel , Cesar

## COMENZAMOS

Ejecutar

```
python3 -m venv env
```

```
source env/bin/activate
```

```
pip install -r requirements.txt
```

## Instalar haarcascade_frontalface_default.xml

```
api/services/haarcascade_frontalface_default.xml
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
```

```
python run.py
```

##Errores

```
face_recognizer = cv2.face.EigenFaceRecognizer_create()
```

```
AttributeError: module 'cv2.cv2' has no attribute 'face'
```

##Solucion 01

```
- pip uninstall opencv-contrib-python

```

```
- pip install opencv-contrib-python
```
