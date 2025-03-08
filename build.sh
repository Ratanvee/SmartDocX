#!/bin/sh

# Create a temporary directory for Ghostscript
mkdir -p /tmp/ghostscript

# Download the Ghostscript binary
curl -L -o /tmp/ghostscript/gs https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10000/ghostscript-10.00.0-linux-x86_64

# Make it executable
chmod +x /tmp/ghostscript/gs

# Run migrations and start Django
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn app.wsgi:application --bind 0.0.0.0:8000
