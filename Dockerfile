FROM python:3.8-alpine

# Set environment variable for PATH
ENV PATH="/scripts:${PATH}"

# Copy necessary files
COPY ./requirements.txt /requirements.txt
COPY ./BillingSystem /BillingSystem
COPY ./scripts /scripts

# ENV HOSTNAME=billingsystem

WORKDIR /BillingSystem

# Update and install dependencies
RUN apk add --update --no-cache --virtual .tmp-deps \
    build-base musl-dev linux-headers && \ 
    python -m venv /opt && /opt/bin/pip install --upgrade pip && \
    /opt/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home user

# Set up working directory and permissions
RUN mkdir -p /vol/web/log/ && \
    chmod -R +x /scripts/ && \
    chown -R user:user /vol/ && \
    chmod -R 755 /vol/ && \
    chown -R user:user /scripts/ && \
    touch /vol/web/log/uwsgi.log && \
    chown user:user /vol/web/log/uwsgi.log && \
    chmod 755 /vol/web/log/uwsgi.log 

RUN /opt/bin/python manage.py collectstatic --noinput

# Switch to non-root user
USER user


EXPOSE 8000
# Set the entrypoint command
CMD ["sh", "-c", "sh /scripts/migrate.sh && sh /scripts/entrypoint.sh"]