#!/bin/bash

echo 'Running Migrations'
python manage.py migrate


echo 'Collecting the static files'
python manage.py collectstatic