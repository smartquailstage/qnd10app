server {
    listen 80;
    server_name ${DOMAIN} quitocultura.${DOMAIN}  164.90.153.177 ;

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location /static {
    alias /qnd10app/qnd10app/static;
    client_max_body_size    1000M;
     }

    location /media {
    alias  /qnd10app/qnd10app/media;
    client_max_body_size    1000M;
     }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 80;
    server_name   quitocultura.${DOMAIN} 164.90.153.177 ;

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location /static {
    alias /qnd10app/qnd10app/static;
    client_max_body_size    1000M;
     }

    location /media {
    alias  /qnd10app/qnd10app/media;
    client_max_body_size    1000M;
     }

    location / {
        return 301 https://$host$request_uri;
    }
}

