#!/usr/bin/env bash

python3 -m pip install -r requirements.txt

echo "Migrando banco de dados..."
python3 filopedia/manage.py makemigrations --noinput
python3 filopedia/manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 filopedia/manage.py collectstatic --noinput
