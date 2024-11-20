#!/bin/bash
docker build -f Dockerfile . -t headpatter.xyz:v0
docker run --rm -it -p 80:8000 --name headpatter.xyz headpatter.xyz:v0


