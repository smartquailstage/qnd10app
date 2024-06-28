FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"

# Instalar bash, postfix, postfix-pcre y mailutils
RUN apk add --no-cache \
    bash \
    postfix \
    postfix-pcre \
    mailutils \
    && rm -rf /var/cache/apk/*

# Copiar certificados SSL
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Copiar configuraciones de Postfix
COPY conf /etc/postfix

# Volumen para el spool de Postfix
VOLUME ["/var/spool/postfix"]

# Punto de entrada
ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

# Exponer el puerto 25 (SMTP)
EXPOSE 25
