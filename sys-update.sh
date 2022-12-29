#!/bin/bash

update() {

os_name=
sudo -u sysbot DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/X_userid/bus notify-send 'Hello world!' 'This is an example notification.';
apt-get update;


apt-get upgrade -y;

    
if [ $? -ne 0 ]; then
    echo "Error al actualzar el sistema"
else 
    echo "Ejecutando el autolimpiado ... "
    apt-get autoclean;
    echo "Limpiando ... "
    apt-get clean;
    echo "Eliminando paquetes innecesarios... "
    apt-get autoremove -y
    echo "El sistema de ha actualzado exitosamente "
    notify-send 'Script Solvetic!' 'El script está listo.' -a 'Script' -u normal -i face-smile        
fi
}
update

otra(){
    notify-send 'Solvetic!' 'Esta es una notificación personal!';

}
otra