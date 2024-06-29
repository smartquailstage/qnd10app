FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"
 
RUN apk add --no-cache bash postfix postfix-pcre 

COPY conf /etc/postfix
COPY conf/vitual /etc/postfix/
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/


VOLUME ["/var/spool/postfix"]

ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

EXPOSE 25
