FROM debian:11-slim

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C
ARG DEBIAN_FRONTEND=noninteractive

# Descargar e importar la clave GPG de Dovecot
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && wget -O- https://repo.dovecot.org/DOVECOT-REPO-GPG | gpg --dearmor > /etc/apt/trusted.gpg.d/dovecot.gpg \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de listas de repositorios de dovecot
COPY dovecot.list /etc/apt/sources.list.d/dovecot.list

# Instalamos paquetes necesarios
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
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
        ssl-cert \
    && rm -rf /var/lib/apt/lists/*

# Configuración adicional
RUN groupadd -g 1000 vmail \
    && useradd -u 1000 -g 1000 -d /srv/vmail -s /sbin/nologin vmail \
    && passwd -l vmail \
    && mkdir -p /srv/mail \
    && chown -R vmail:vmail /srv/mail \
    && make-ssl-cert generate-default-snakeoil \
    && mkdir -p /etc/dovecot \
    && ln -s /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/dovecot/cert.pem \
    && ln -s /etc/ssl/private/ssl-cert-snakeoil.key /etc/dovecot/key.pem

# Copiamos el archivo de configuración de Dovecot
COPY dovecot.conf /etc/dovecot/dovecot.conf

# Exponemos los puertos
EXPOSE 24 110 143 587 990 993 4190

# Volumen para configuraciones y datos
VOLUME ["/etc/dovecot", "/srv/mail"]

# Punto de entrada y comando por defecto
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
