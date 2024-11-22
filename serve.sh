#!/bin/bash
docker stop headpatter.xyz
docker build -f Dockerfile . -t headpatter.xyz:v0
docker run --env-file ./site.env --rm -it -p 80:8000 --name headpatter.xyz headpatter.xyz:v0
