FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11

# additional python packages
RUN apk add build-base python3-dev libffi-dev

# install py dependencies
COPY ./backend/app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# copy rest of py code
COPY ./backend/app /app

ENV MODULE_NAME app
ENV STATIC_PATH /app/app/static