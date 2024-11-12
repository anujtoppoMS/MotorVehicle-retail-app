FROM python:3.8-alpine

# Set environment variable for PATH
ENV PATH="/scripts:/opt/bin:${PATH}"

# Copy necessary files
COPY ./requirements.txt /requirements.txt
COPY ./BillingSystem /BillingSystem
COPY ./scripts /scripts

WORKDIR /BillingSystem

# Update and install dependencies
RUN apk add --update --no-cache --virtual .tmp-deps \
    build-base musl-dev linux-headers && \ 
    python -m venv /opt && /opt/bin/pip install --upgrade pip && \
    /opt/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home user

# Set up working directory and permissions
RUN mkdir -p /vol/web/static && \
    chmod -R +x /scripts/ && \
    chown -R user:user /vol && \
    chown -R user:user /scripts/ && \
    chmod -R 755 /vol/

# Switch to non-root user
USER user

# Print the PATH for debugging
RUN echo ${PATH}

# Set the entrypoint command
CMD ["/scripts/entrypoint.sh"]
