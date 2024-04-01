server {
    listen                     ${LISTEN_PORT};
    server_name                127.0.0.1 localhost 164.90.153.177 0.0.0.0; 
    
location /static {
    alias /qnd10app/qnd10app/qnd10app/static;
    client_max_body_size    1000M;
}

location /media {
    alias  /qnd10app/qnd10app/qnd10app/media;
    client_max_body_size    1000M;
}

location / {
    uwsgi_pass              ${APP_HOST}:${APP_PORT};
    include                 /etc/nginx/uwsgi_params;
    client_max_body_size    1000M;
    }    

}


    




