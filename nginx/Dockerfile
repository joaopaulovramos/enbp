FROM nginx:1.25-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./proxy/* /etc/nginx/

RUN apk add --no-cache openssl bash


VOLUME /vol/static
VOLUME /vol/www
VOLUME /vol/media

CMD [ "/run.sh" ]

