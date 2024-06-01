FROM mysql:8.2.0
ENV MYSQL_ROOT_PASSWORD='1234'
ENV MYSQL_DATABASE=compraAhorra
#COPY ./scripts/ /docker-entrypoint-initdb.d/