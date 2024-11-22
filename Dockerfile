FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app
RUN mkdir -p /app/static

RUN  pip3 install flask pyopenssl Flask-FlatPages Pygments pillow

COPY ./server.py /app
COPY ./headpatter.xyz.cfg /app
COPY ./headpatter.db /app
ADD ./content /app/content
ADD ./templates /app/templates
ADD ./utils /app/utils
ADD ./static /app/static
RUN pygmentize -S emacs -f html -a .codehilite > static/pygs.css

ENTRYPOINT ["python3"]
CMD ["server.py"]

EXPOSE 8000
