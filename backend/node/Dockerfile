FROM node:10

WORKDIR /code

COPY ./frontend/package.json /code/
RUN npm install

# only copy the rest afterwards so that the npm install can be cached
COPY ./frontend /code

COPY ./backend/node/build.sh build.sh
RUN chmod 750 ./build.sh
CMD ["./build.sh"]
