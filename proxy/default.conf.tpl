upstream billingsystem {
    server billingsystem:8000;
}

server {
    listen 8080;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass billingsystem;
        include /etc/nginx/uwsgi_params;
    }
}