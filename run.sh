#!/bin/bash

#workon autorepost
cd /home/ramdani/projects/auto-repost

while true; do
    python AutoPost.py
    python instascraper.py
    sleep 30
done
