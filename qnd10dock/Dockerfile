FROM python:3.11.6-alpine3.18
LABEL maintainer="mau_dev@smartquail.io"

ENV PYTHONUNBUFFERED 1

ENV NODE_VERSION=qnd10app
ENV NODE_APP_NAME=qnd10app
ENV USER=qnd10

RUN apk add --no-cache git
ARG username=smartquailDev
ARG password=ms1719183830
RUN git clone https://github.com/smartquailstage/${NODE_VERSION}.git

COPY ./12012023.txt /12012023.txt
COPY ./scripts /scripts
COPY ./uwsgi_stage.ini /${NODE_VERSION}/${NODE_APP_NAME}/uwsgi_stage.ini
COPY ./baton.min.js /${NODE_VERSION}/${NODE_APP_NAME}/baton.min.js
COPY ./qnode_ascii-art.txt /${NODE_VERSION}/${NODE_APP_NAME}/qnode_art.txt

WORKDIR /${NODE_VERSION}/${NODE_APP_NAME}

EXPOSE 9000

RUN python3.11 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps build-base curl postgresql-dev gcc musl-dev python3-dev linux-headers libffi-dev py3-cffi py3-cryptography jpeg-dev go zlib-dev libjpeg wget fontconfig ttf-freefont font-noto terminus-font gtk+3.0 pango busybox-extras openssl-dev gettext neofetch && \
    /py/bin/pip install -r /12012023.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home ${USER} && \
    mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/static && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/static  && \
    mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/media && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/media  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/media && \
    mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/static && \
    mkdir -p /var/log/uwsgi/ && \
    chown -R ${USER}:${USER} /var/log/uwsgi/ && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/ && \
    chmod -R 755 /scripts  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/ &&\
    chmod -R u+x /scripts/uwsgi.sh &&\
    chmod -R +x /scripts && \
    rm /py/lib/python3.11/site-packages/baton/static/baton/app/dist/baton.min.js && \
    cp /${NODE_VERSION}/${NODE_APP_NAME}/baton.min.js  /py/lib/python3.11/site-packages/baton/static/baton/app/dist/

ENV PATH="/scripts:/py/bin:$PATH"

RUN apk add --no-cache --update musl musl-utils musl-locales tzdata && \
    cp /usr/share/zoneinfo/America/Guayaquil /etc/localtime && \
    echo 'export LC_ALL=es_ES.UTF-8' >> /etc/profile.d/locale.sh && \
    sed -i 's|LANG=C.UTF-8|LANG=es_ES.UTF-8|' /etc/profile.d/locale.sh

ENV TZ=America/Guayaquil \
    LANG=es_ES.UTF-8 \
    LANGUAGE=es_ES.UTF-8

USER ${USER}

CMD ["uwsgi.sh"]
