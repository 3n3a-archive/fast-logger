#!/bin/bash
#
# Start Uvicorn Server on Public IP
#
# Enea Krähenbühl, 2022

mkdir uploads
pip3 install -qqq -r requirements.txt # super quiet pip
python3 -m uvicorn main:app --host 0.0.0.0