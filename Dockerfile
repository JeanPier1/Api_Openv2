FROM python:3.8.5-alpine


# # Step 2 tell what you want to do
RUN apk update && \
    apk update --no-cache --update build-base &&\
    apk add --virtual buwild-deps gcc python3-dev musl-dev && \
    apk add netcat-openbsd && \
    apk add --no-cache tini git && \
    apk add --update npm &&\
    apk add python3 &&\
    apk add py3-pip &&\
    apk add --no-cache openssl-dev libffi-dev &&\
    apk add --update --no-cache  python3-dev python3 libffi-dev libressl-dev bash git gettext curl &&\
    apk add --no-cache --virtual .build-deps build-base linux-headers &&\
    apk add --no-cache jpeg-dev zlib-dev &&\
    apk add --no-cache cmake &&\
    apk add --no-cache gtk+2.0


WORKDIR /api-opencv
RUN mkdir controllers
RUN mkdir data
RUN mkdir middllewares
RUN mkdir models
RUN mkdir routes
RUN mkdir services
RUN mkdir static
RUN mkdir templates
RUN mkdir test

COPY requirements.txt /api-opencv
# agregando e instalando requerimientos
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
#RUN rm -it \
#     apk -E DISPLAY=${DISPLAY} \
#     apk --privileged \
#     apk -v /tmp/.X11-unix:/tmp/.X11-unix \
#     apk --device=/dev/video0:/dev/video0 \
#     apk --ipc=host maskrcnn-benchmark \
#     apk python services/opencvservice_reconocimiento.py \
#     apk python services/opencvservice_recopilacion.py \
#     apk --min-image-size 300 \
#     apk MODEL.DEVICE cpu

EXPOSE 5001

ADD /api/controllers/ /api-opencv/controllers/
COPY /api/controllers/ /api-opencv/controllers/
#
ADD /api/data/ /api-opencv/data/
COPY /api/data/ /api-opencv/data/
#
ADD /api/middlewares/ /api-opencv/middllewares/
COPY /api/middlewares/ /api-opencv/middllewares/
#
ADD /api/models/ /api-opencv/models/
COPY /api/models/ /api-opencv/models/
#
ADD /api/routes/ /api-opencv/routes/
COPY /api/routes/ /api-opencv/routes/
#
ADD /api/services/ /api-opencv/services/
COPY /api/services/ /api-opencv/services/
#
ADD /api/static/ /api-opencv/static/
COPY /api/static/ /api-opencv/static/

#
ADD /api/static/ /api-opencv/static/
COPY /api/static/ /api-opencv/static/
#
ADD /api/templates/ /api-opencv/templates/
COPY /api/templates/ /api-opencv/templates/
#
ADD /api/test/ /api-opencv/test/
COPY /api/test/ /api-opencv/test/

COPY /api/app.py  /api-opencv
COPY run.py  /api-opencv

ENTRYPOINT ["python3"]
CMD [ "run.py"]
