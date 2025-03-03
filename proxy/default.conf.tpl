upstream billingsystem {
    server ${SERVER_NAME}:${SERVER_PORT};
}

server {
    listen 443 ssl;
    server_name billingsystem;

    ssl_certificate /etc/ssl/certs/my_certificate.crt;
    ssl_certificate_key /etc/ssl/private/my_private.key;

    # Redirect all HTTP requests to HTTPS
    location / {
        proxy_pass http://billingsystem;
        include /etc/nginx/uwsgi_params;    
    }
    location /static {
        alias ${STATIC_LOCATION};
    }
}