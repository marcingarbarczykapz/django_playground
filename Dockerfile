FROM python:3.11.5

RUN apt-get update && \
    apt-get install -y locales locales-all && \
    locale-gen pl_PL

COPY requirements/ /requirements

RUN pip install -r requirements/requirements.txt

COPY dev /develop

RUN chmod +x /develop/web/entrypoint.sh && \
    chmod +x /develop/celery/entrypoint.sh

COPY / /app/

WORKDIR /app