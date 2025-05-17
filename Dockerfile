FROM apache/superset:latest

USER root

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install mysqlclient psycopg2 authlib

ENV DATABASE $DATABASE

COPY /config/superset_init.sh ./superset_init.sh
RUN chmod +x ./superset_init.sh

COPY /config/superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py
ENV SECRET_KEY $SECRET_KEY
ENV GOOGLE_CLIENT_ID $GOOGLE_CLIENT_ID
ENV GOOGLE_SECRET $GOOGLE_SECRET

USER superset

ENTRYPOINT [ "./superset_init.sh" ]
