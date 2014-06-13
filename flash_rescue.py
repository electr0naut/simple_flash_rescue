__author__ = 'ub'
# -*- coding: utf-8 *-*
#! /usr/bin/env python

# pendiente: chequear por browsers, mirar mas browsers
# para ripear, añadir strings de fechas a carpetas
# avisa de sudo, mirar verbose version. Multiplataforma? cvs? output to file?
# solo explorar las carpetas en busca de caches
# descargar o visualizar info
# descargar solo despues de una fecha
# descargar desde antes de una fecha
# modo continuo? extraer continuamente en base a unos parametros?
# pendiente de verificar modo interactivo
# parser.add_argument('-i', '--interactive', action='store_true', default=False,
# help='Interactive behaviour', dest='interactive')

import sys
import os
import argparse

supp_browsers = (
    'firefox',
    'chrome'
)

home_path = 'HOME'

parser = argparse.ArgumentParser(
    description='Recover flash files from browsers cache')

parser.add_argument('-b', '--browser', action='store',
                    choices=[str(browser) for browser in supp_browsers],
                    type=str, dest='browser')

cmds_path = parser.add_mutually_exclusive_group(required=True)

cmds_path.add_argument('-s', '--short-path', nargs='?', action='store',
                       type=str, default=os.getenv('HOME'),
                       help='Destination path for the files appended to $HOME from current user',
                       dest='from_home_path')

cmds_path.add_argument('-l', '--long-path', nargs=1, action='store', type=str,
                       help='Absolute destination path for the files', dest='absolute_path')

cmds_files = parser.add_mutually_exclusive_group(required=True)

cmds_files.add_argument('-d', '--deleted-only', action='store_true',
                        default=False, help='Recover only flash files from closed tabs',
                        dest='deleted')

cmds_files.add_argument('-c', '--cached-active', action='store_true',
                        default=False, help='Recover only flash files from browsers active tabs',
                        dest='cached')

cmds_files.add_argument('-a', '--all-recovery', action='store_true',
                        default=False, help='Recover every flash file available from browser',
                        dest='all')

args = parser.parse_args()

print
args.__dict__