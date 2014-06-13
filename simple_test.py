__author__ = 'ub'
import subprocess
import random
import os
import sys
import string


def check_arguments():
    output = subprocess.getstatusoutput('sudo lsof|grep FlashXX')
    riau = output[1:]
    ruta = riau[0]
    output = ruta.split('\n')

    comando_final = 'ls ' + ruta

    for line in output:
        temp = line.split()

        if ((temp[3].strip('u')).isdigit()):
            semilla = ''.join(random.choice(string.letters + string.digits) for i in range(10)) + '.flv'
            comando_final = ''.join(['sudo cp /proc/' + temp[1] + '/fd/' + temp[3].strip('u') + ' ' + ruta + semilla])
            subprocess.getstatusoutput(comando_final)
            riau2 = 'sudo chown max ' + ruta + semilla  # change max to own user
            subprocess.getstatusoutput(riau2)
            print(ruta + semilla)
    subprocess.getstatusoutput(
        'sudo ls -lrt /home/max/Videos/.stream/')  # change max to own user, maybe target also changed
    print('fin')


def main(argv=None):
    if (len(sys.argv) > 1):
        if (os.path.isdir(sys.argv[1])):
            ruta = sys.argv[1]
        else:
            if (os.path.isdir(os.path.expanduser('~' + sys.argv[1]))):
                ruta = ''.join([os.path.expanduser('~') + '/' + sys.argv[1]])
