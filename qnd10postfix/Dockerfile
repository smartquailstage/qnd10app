FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"

# Instalar curl y otras dependencias necesarias para compilar Postfix y para PostgreSQL
RUN apk add --no-cache \
    bash \
    build-base \
    linux-pam-dev \
    openssl-dev \
    pcre-dev \
    postgresql-dev \
    postgresql-client \
    cyrus-sasl-dev \
    curl

# Copiar el archivo postfix-3.7.11.tar.gz desde tu contexto local al contenedor
COPY postfix-3.7.11.tar.gz /tmp/postfix-3.7.11.tar.gz
RUN tar -zxvf /tmp/postfix-3.7.11.tar.gz -C /tmp/
# Descargar y compilar Postfix con soporte para PostgreSQL
RUN cd /tmp/postfix-3.7.11 && \
    make makefiles CCARGS="-DHAS_PCRE -DUSE_TLS -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl -DUSE_PCRE -DDEF_SERVER_SASL_TYPE=CYRUS -DDEF_SERVER_SASL_PATH=\"/var/spool/postfix/private/auth\"" AUXLIBS="-lpcre -lsasl2" && \
    make && make install

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