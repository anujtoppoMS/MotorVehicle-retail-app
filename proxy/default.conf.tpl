upstream billingsystem {
    server billingsystem:8000;
}

server {
    listen 8000;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass proxy-app:8080;
        include /etc/nginx/uwsgi_params;
    }
}
