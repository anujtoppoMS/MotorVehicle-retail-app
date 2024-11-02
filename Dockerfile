# FROM python:3.9.7-slim

# COPY . /app
# WORKDIR /app

# RUN python3 -m venv /opt/venv

# RUN /opt/venv/bin/pip install pip --upgrade && \
#     /opt/venv/bin/pip install -r requirements.txt && \
#     chmod +x entrypoint.sh

# CMD ["/app/entrypoint.sh"]


FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /BillingSystem
COPY ./BillingSystem /BillingSystem
WORKDIR /BillingSystem
RUN mkdir /scripts
COPY ./scripts /scripts
RUN chmod +x /scripts/entrypoint.sh

RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol && chown -R user:user /scripts/
RUN chmod -R 755 /vol/web
USER user
RUN echo ${PATH}

CMD ["/scripts/entrypoint.sh"]