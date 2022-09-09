#!/usr/bin/env python3
import os


# this will use the dtabase seetting for openshift posgresql database already deployed
os.system("python3 ./manage.py migrate")

# connect to pod to change password before setting route for pod
superuser="from django.contrib.auth.models import User; User.objects.create_superuser('djangoadmin', 'djangoadmin@example.com', 'm2iformation')"

# create superuser django no input
#os.system("python3 manage.py shell -c "${superuser}"")

# create the log file
os.system("touch logs_webApp.log")

# this will use gunicorn to run the server ans start the app that will serve on port 8000 natively but changed to prot 8080 with option -b
os.system("gunicorn --env DJANGO_SETTINGS_MODULE=webApp.settings webApp.wsgi -b :8080")
