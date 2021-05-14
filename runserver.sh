#!/bin/sh
#
#### Check port 
#netstat -lanp | grep
#ss -p | grep
#

#####################################################
#                          Configuracion del server #
#####################################################
IP_SERVER='127.0.0.1'
PORT_SERVER='8080'
DJANGO_APP=$(dirname $(readlink -f $0))
DJANGO_SERVER=$(dirname $DJANGO_APP)
NAME="${DJANGO_APP##*/}" 
DJANGO_ENV_PATH=$DJANGO_SERVER/python_venvs/hands_on


#####################################################
#                              Ejecucion del server #
# Se crea un archivo temp donde se almacenan los    #
# comandos a ejecutar                               #
# Se crea un screen con el archivo temp             #
# Se elimina el archivo temp                        #
#####################################################
if screen -list | grep -q "$NAME"
then 
    echo "Deteniendo $NAME"
    screen -X -S $NAME quit
fi
echo "Ejecutando $NAME"
tempfile=$(mktemp)
cat > $tempfile <<EOF
. $DJANGO_ENV_PATH/bin/activate
cd $DJANGO_APP
python manage.py runserver "$IP_SERVER:$PORT_SERVER"
EOF
screen -dm -S "$NAME" /bin/bash
screen -X -S "$NAME" readbuf $tempfile
screen -X -S "$NAME" paste .
rm -f $tempfile
echo "App $NAME corriendo en $IP_SERVER:$PORT_SERVER"