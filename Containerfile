FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \

COPY requirements.txt .
RUN python -m pip install --requirement requirements.txt
