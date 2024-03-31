server {
    listen         443 ssl;
    server_name    ${DOMAIN} ;

    ssl_certificate     /etc/letsencrypt/live/${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/${DOMAIN}/privkey.pem;

    include     /etc/nginx/options-ssl-nginx.conf;

    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location /static {
         alias /qnd10app/qnd10app/qnd10app/staticfiles;
         client_max_body_size    1000M;
    }

    location /media {
    alias /qnd10app/qnd10app/qnd10app//media;
    client_max_body_size    1000M;
    }


    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 1000M;
    }
}


server {
    listen         443 ssl;
    server_name    quitocultura.${DOMAIN} ;

    ssl_certificate     /etc/letsencrypt/live/quitocultura.${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/quitocultura.${DOMAIN}/privkey.pem;

    include     /etc/nginx/options-ssl-nginx.conf;

    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location /static {
         alias /qnd10app/qnd10app/qnd10app/staticfiles;
         client_max_body_size    1000M;
    }

    location /media {
        alias /qnd10app/qnd10app/qnd10app/media;
        client_max_body_size    1000M;
    }


    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 1000M;
    }
}


