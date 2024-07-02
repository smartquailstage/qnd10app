FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"

# Instalar curl, tar, make y otras dependencias necesarias para compilar Postfix y PostgreSQL
RUN apk add --no-cache bash build-base linux-pam-dev  openssl-dev   pcre-dev postgresql-client  postfix-pgsql postfix postfix-pcre   cyrus-sasl-dev

# Copiar el archivo postfix-3.8.5.tar.gz desde tu contexto local al contenedor

# Copiar la configuración de Postfix
COPY conf /etc/postfix

# Copiar certificados SSL
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Crear el directorio y dar permisos adecuados
RUN mkdir -p /var/spool/postfix/private/transport \
    && chown postfix:postfix /var/spool/postfix/private/transport \
    && chmod 750 /var/spool/postfix/private/transport

# Volumen para el directorio spool de Postfix
VOLUME ["/var/spool/postfix"]

# Entrypoint para iniciar Postfix
ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

# Exponer el puerto SMTP (25)
EXPOSE 25
