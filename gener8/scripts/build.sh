#!/usr/bin/env bash

# $IMAGE_NAME var is injected into the build so the tag is correct.

echo "Build hook running"
docker build --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
             --build-arg VCS_REF=`git rev-parse --short HEAD` \
             -t $IMAGE_NAME .
