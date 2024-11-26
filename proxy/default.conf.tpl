
server {
    listen 80;
    server_name billingsystem;

    # Redirect all HTTP requests to HTTPS
    location / {
        proxy_pass http://billingsystem-service:8000;
        include /etc/nginx/uwsgi_params;        
    }
    location /static {
        alias /vol/static;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name billingsystem;
    ssl_certificate /etc/ssl/certs/my_certificate.crt;
    ssl_certificate_key /etc/ssl/private/my_private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    location / {
        proxy_pass http://billingsystem-service:8000;
        include /etc/nginx/uwsgi_params;
    }

    location /static {
        alias /vol/static;
    }
}