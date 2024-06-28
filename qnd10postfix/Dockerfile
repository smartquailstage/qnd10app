FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io>"

# Instalar bash, postfix, postfix-pcre, mailutils y OpenSSL
RUN apk add --no-cache \
    bash \
    postfix \
    postfix-pcre \
    mailutils \
    openssl \
    && rm -rf /var/cache/apk/*

# Copiar certificados SSL
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Configurar Postfix
COPY conf /etc/postfix
RUN postconf -e "myhostname = mail.smartquail.io" \
    && postconf -e "mydomain = smartquail.io" \
    && postconf -e "myorigin = \$mydomain" \
    && postconf -e "mydestination = \$myhostname, localhost.\$mydomain, localhost, \$mydomain" \
    && postconf -e "smtp_tls_security_level = may" \
    && postconf -e "smtpd_tls_cert_file = /etc/ssl/certs/fullchain.pem" \
    && postconf -e "smtpd_tls_key_file = /etc/ssl/private/privkey.pem" \
    && postconf -e "smtpd_tls_security_level = may" \
    && postconf -e "smtpd_tls_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1" \
    && postconf -e "relayhost = [smtp.gmail.com]:587" \
    && postconf -e "smtp_use_tls = yes" \
    && postconf -e "smtp_sasl_auth_enable = yes" \
    && postconf -e "smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd" \
    && postconf -e "smtp_sasl_security_options = noanonymous"

# Crear archivo sasl_passwd
RUN echo "[smtp.gmail.com]:587    phys.mauricio.silva@gmail.com:ms95355672" > /etc/postfix/sasl_passwd
RUN postmap /etc/postfix/sasl_passwd
RUN chmod 600 /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db

# Volumen para el spool de Postfix
VOLUME ["/var/spool/postfix"]

# Punto de entrada
ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

# Exponer el puerto 25 (SMTP)
EXPOSE 25