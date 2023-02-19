#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python SignupDirector/manage.py collectstatic --no-input
python SignupDirector/manage.py migrate
