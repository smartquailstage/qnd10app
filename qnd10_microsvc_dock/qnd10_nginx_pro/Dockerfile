FROM FROM nginx:1.24.0-alpine-slim

COPY ./nginx/* /etc/nginx/
COPY ./ssl-certs-smartquail/* /etc/nginx/
COPY ./nginx/run.sh /run.sh
COPY ./ssl-certs-smartquail/https/smartquail.io/* /etc/letsencrypt/live/smartquail.io/
COPY ./ssl-certs-smartquail/https/quitocultura.smartquail.io/* /etc/letsencrypt/live/quitocultura.smartquail.io/


ENV DOMAIN=smartquail.io
ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnd10app:9000
ENV APP_HOST=qnd10app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

RUN mkdir -p /qnd10app/qnd10app/staticfiles && \
    chmod 755 /qnd10app/qnd10app/staticfiles && \
    mkdir -p  /qnd10app/qnd10app/media && \
    chmod 755 /qnd10app/qnd10app/media && \
    mkdir -p /qnd10app/qnd10app/static && \
    chmod 755 /qnd10app/qnd10app/static 

VOLUME /qnd10app/qnd10app/staticfiles
VOLUME /qnd10app/qnd10app/mediafiles
VOLUME /qnd10app/qnd10app/static
VOLUME /vol/www
VOLUME /vol/proxy
VOLUME /etc/letsencrypt

CMD ["/run.sh" , "/run_2.sh"]