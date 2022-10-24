FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/geoapi

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN apk add --no-cache geos gdal

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY geoapi/entrypoint.sh .

COPY . .

RUN chmod +x /usr/src/geoapi/entrypoint.sh
ENTRYPOINT ["/usr/src/geoapi/entrypoint.sh"]