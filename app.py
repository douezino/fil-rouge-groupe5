#!/usr/bin/env python3
import os


# this will use the dtabase seetting for openshift posgresql database already deployed
os.system("./manage.py migrate --database=openshiftpostgresql")

# this will use gunicorn to run the server ans start the app that will serve on port 8000
os.system("gunicorn --env DJANGO_SETTINGS_MODULE=webApp.settings webApp.wsgi")
