#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

python SignupDirector/manage.py collectstatic --no-input
python SignupDirector/manage.py migrate
