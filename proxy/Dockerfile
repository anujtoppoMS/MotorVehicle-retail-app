FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

USER root
COPY ./my_certificate.crt /etc/ssl/certs/my_certificate.crt
COPY ./my_private.key /etc/ssl/private/my_private.key

# ENV HOSTNAME proxy

# Ensure the /tmp directory is present and writable

RUN mkdir -p /static/

RUN chmod 755 /etc/ssl/certs/my_certificate.crt && \
    chmod 755 /etc/ssl/private/my_private.key && \
    chown nginx:nginx /etc/ssl/certs/my_certificate.crt && \
    chown nginx:nginx /etc/ssl/private/my_private.key
RUN chmod 755 /static/ && \
    touch /etc/nginx/conf.d/default.conf && \
    chown -R nginx:nginx /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /run.sh && \
    chown -R nginx:nginx /static/ && \
    chmod +x /run.sh


USER nginx
EXPOSE 443

ENTRYPOINT [ "sh","-c","sh /run.sh" ]