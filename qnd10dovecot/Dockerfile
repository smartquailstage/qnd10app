FROM debian:11-slim

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C
ARG DEBIAN_FRONTEND=noninteractive

# Añadir la clave GPG de Dovecot
ADD dovecot.gpg /etc/apt/keyrings/dovecot.gpg
# Añadir el archivo de lista de repositorios de Dovecot
ADD dovecot.list /etc/apt/sources.list.d

# Copiar los certificados al directorio /etc/dovecot/
COPY mail.smartquail.io/certs/fullchain.pem /etc/dovecot/fullchain.pem
COPY mail.smartquail.io/private/privkey.pem /etc/dovecot/privkey.pem

# Cambiar los permisos de los certificados
RUN chmod 600 /etc/dovecot/fullchain.pem /etc/dovecot/privkey.pem

# Actualizar e instalar paquetes necesarios
RUN apt-get -y update && apt-get -y install \
    tini \
    dovecot-core \
    dovecot-gssapi \
    dovecot-imapd \
    dovecot-ldap \
    dovecot-lmtpd \
    dovecot-lua \
    dovecot-managesieved \
    dovecot-mysql \
    dovecot-pgsql \
    dovecot-pop3d \
    dovecot-sieve \
    dovecot-solr \
    dovecot-sqlite \
    dovecot-submissiond \
    ca-certificates \
    ssl-cert && \
    rm -rf /var/lib/apt/lists && \
    groupadd -g 1000 vmail && \
    useradd -u 1000 -g 1000 vmail -d /srv/vmail && \
    passwd -l vmail && \
    rm -rf /etc/dovecot && \
    mkdir /srv/mail && \
    chown vmail:vmail /srv/mail 

# Añadir los archivos de configuración de Dovecot
ADD dovecot.conf /etc/dovecot/dovecot.conf
ADD dovecot-sql.conf.ext /etc/dovecot/dovecot-sql.conf.ext

# Exponer los puertos necesarios
EXPOSE 24
EXPOSE 110
EXPOSE 143
EXPOSE 587
EXPOSE 990
EXPOSE 993
EXPOSE 4190

# Volumen para datos persistentes
VOLUME ["/etc/dovecot", "/srv/mail"]

# Punto de entrada y comando predeterminado
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
