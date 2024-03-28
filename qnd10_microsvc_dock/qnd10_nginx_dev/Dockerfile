FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="smartquail.io"

#COPY ./ssl/qnode41_app.crt /etc/nginx/ssl/qnode0_app.crt
#COPY ./ssl/qnode0_app.key /etc/nginx/ssl/qnode0_app.key
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh


ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnd30_app_stg:9000
ENV APP_HOST=qnd30_app_stg
ENV APP_PORT=9000

USER root

RUN mkdir -p /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/staticfiles && \
    chmod 755 /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/staticfiles && \
    mkdir -p /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/media && \
    chmod 755 /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/media && \
    mkdir -p /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/static && \
    chmod 755 /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/static && \

    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/staticfiles
VOLUME /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/mediafiles
VOLUME /qnd30_app_stg/qnd30_app_stg/qnd30_app_stg/static

USER nginx
#ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/run.sh"]