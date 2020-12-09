PROJECTO PREVIO

Ejecutar

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python run.py

Errores
\*01
face_recognizer = cv2.face.EigenFaceRecognizer_create()
AttributeError: module 'cv2.cv2' has no attribute 'face'

Solucion
\*01

- pip uninstall opencv-contrib-python
- pip install opencv-contrib-python

Creditos:

Edson
Abdiel
