# Build Vue Application
FROM node:14 AS ui
WORKDIR /vue-app 
COPY axon_ui/package.json /vue-app 
COPY axon_ui/package.lock /vue-app
RUN yarn 
COPY axon_ui/. /vue-app 
RUN yarn build

# Install Python Packages
FROM python:3.8-alpine
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

# Actual loading
COPY manage.py /app
COPY axon_server/. /app/axon_server
COPY orgroam/. /app/orgroam
COPY run-server.sh /app
COPY migrate.sh /app

COPY --from=ui /vue-app/dist /app/axon_ui/dist
RUN chmod +x /app/run-server.sh
RUN chmod +x /app/migrate.sh

# Start server.
EXPOSE 8080
WORKDIR /app
CMD ["./run-server.sh"]
