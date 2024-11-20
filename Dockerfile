FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

RUN  pip3 install flask pyopenssl Flask-FlatPages Pygments
COPY . /app

ENTRYPOINT ["python3"]
CMD ["server.py"]

EXPOSE 8000
