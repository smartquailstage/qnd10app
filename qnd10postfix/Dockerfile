FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"
 
RUN apk add --no-cache bash postgresql-client postfix postfix-pcre  cyrus-sasl

COPY conf /etc/postfix

COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Crear el directorio y dar permisos adecuados
RUN mkdir -p /var/spool/postfix/private/transport \
    && chown postfix:postfix /var/spool/postfix/private/transport \
    && chmod 750 /var/spool/postfix/private/transport

VOLUME ["/var/spool/postfix/private/transport"]
VOLUME ["/var/spool/postfix"]

ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

EXPOSE 25
