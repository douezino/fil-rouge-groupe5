Projet Groupe 5 - webApp
We are deploying the app to Openshift
We use command line OP CLI for that:

The setting.py has 2 different database settings, one default and another one for openshift:
To run migrations for both:

./manage.py migrate --database=default
./manage.py migrate --database=openshiftpostgresql
OR either of the commands for one migration.

We use gunicorn to serve the app in the pod and have a script in app/py that will migrate the database and runserver



Deployment:
- Your postgresql database:
oc new-app postgresql POSTGRESQL_USER=<your_user_name> POSTGRESQL_DATABASE=<your_database_name> POSTGRESQL_PASSWORD=<your_password>

- Your github repo app (Openshift will recogniwe and read from app.py):
oc get pods -o wide # to get the ip address of your Openshift deployed postgresql IP address
oc new-app --strategy=source <openshift_compatible_os_image>~<your_github_repo_url>.git#<your_branch> DJANGO_SECRET_KEY="<set_a_long_secret_key_string>" POSTGRESQL_PASSWORD=<your_password> POSTGRESQL_HOST=’<your_openshift_deployed_postgresql_IP_address>’
We successfully used: centos/python-38-centos7

-Test-