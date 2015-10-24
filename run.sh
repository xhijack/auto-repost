#!/bin/bash

#workon autorepost
cd /home/ramdani/projects/auto-repost

while true; do
    python AutoPost.py
    sleep 3600
done
