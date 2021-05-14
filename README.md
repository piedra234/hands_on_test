# hands_on_test
test for mas global application

################
# Requirements #To Do: remove unnecessary packages
################
asgiref==3.3.4
certifi==2020.12.5
cffi==1.14.5
chardet==4.0.0
coreapi==2.3.3
coreschema==0.0.4
coverage==5.5
cryptography==3.4.7
defusedxml==0.7.1
Django==3.2.3
django-cors-headers==3.7.0
django-filter==2.4.0
django-guardian==2.3.0
django-oauth-toolkit==1.5.0
djangorestframework==3.12.4
djangorestframework-csv==2.1.0
djangorestframework-xml==2.0.0
djangorestframework-yaml==2.0.0
-e git+https://github.com/cedadev/dot-restrict-scopes.git@19a4327437c1718bd255772d86aa1f09e5851f9a#egg=dot_restrict_scopes
drf-renderer-xlsx==0.4.0
drf-yasg==1.20.0
drfdocs==0.0.11
et-xmlfile==1.1.0
idna==2.10
inflection==0.5.1
itypes==1.2.0
Jinja2==3.0.0
jwcrypto==0.8
Markdown==3.3.4
MarkupSafe==2.0.0
oauthlib==3.1.0
openpyxl==3.0.7
packaging==20.9
pipdeptree==2.0.0
pkg-resources==0.0.0
pycparser==2.20
Pygments==2.9.0
pyparsing==2.4.7
pytz==2021.1
PyYAML==5.4.1
requests==2.25.1
ruamel.yaml==0.17.4
ruamel.yaml.clib==0.2.2
six==1.16.0
sqlparse==0.4.1
unicodecsv==0.14.1
uritemplate==3.0.1
urllib3==1.26.4

###################
# Running on venv #
###################
sh runserver.sh 
#Change network options 
IP_SERVER='127.0.0.1'
PORT_SERVER='8080'
#Change network option
DJANGO_ENV_PATH=$DJANGO_SERVER/python_venvs/hands_on

##################
# URL            #
##################
api/employees
api/employees/<int:idEmployee>

employees # view covers both api functionalities
