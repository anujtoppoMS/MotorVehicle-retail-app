upstream billingsystem {
    server billingsystem:8020;
}

server {
    listen 8000;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass billingsystem;
        include /etc/nginx/uwsgi_params;
    }
}
