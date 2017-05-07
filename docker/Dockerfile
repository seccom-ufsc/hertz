FROM python:3.6

WORKDIR /home

COPY requirements.txt .
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/bin/dumb-init

RUN chmod +x /usr/bin/dumb-init && \
    chmod +x wait-for-it.sh && \
    pip install -r requirements.txt

VOLUME /code
WORKDIR /code

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
