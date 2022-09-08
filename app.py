#!/usr/bin/env python3
import os


# this will use the dtabase seetting for openshift posgresql database already deployed
<<<<<<< HEAD
os.system("python3 ./manage.py migrate --database=openshiftpostgresql")
=======
os.system("python3 ./manage.py migrate")
>>>>>>> dev

# this will use gunicorn to run the server ans start the app that will serve on port 8000 natively but changed to prot 8080 with option -b
os.system("gunicorn --env DJANGO_SETTINGS_MODULE=webApp.settings webApp.wsgi -b :8080")
