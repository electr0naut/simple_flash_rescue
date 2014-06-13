__author__ = 'ub'
import subprocess
import magic

# ALL UNTESTED

# cache_dir_locator(base_path, options): recibe una string con la ruta al
# directorio de cache correspondiente y una lista de opciones.
# Devuelve una lista con los directorios de cache encontrados
# Opciones tratadas
# firefox_only:
# chrome_only:
# all:


def cache_dir_locator(base_path, options):
    com = ''.join('find ' + base_path + '-name Cache -type d ')
    if 'firefox_only' in options:
        com = ''.join(com + '| grep firefox')
    elif 'chrome_only' in options:
        com = ''.join(com + '| grep chrome')
    elif 'all' in options:
        return subprocess.getstatusoutput(com)
    else:
        return 'OPTIONS ERROR ON cache_dir_locator'
    return subprocess.getstatusoutput(com)


# cache_crawler(path_to_cache_dir, options): recibe una string conteniendo
# el directorio de cache a explorar y una lista de opciones.
# Devuelve una lista con los ficheros de cache localizados
# Opciones tratadas:
# firefox_path:
# chrome_path: (pendiente regex)


def cache_crawler(path_to_cache_dir, options):
    firefox_grep = '[Cache]/[[:alnum:]]{1}[/][[:alnum:]]{2}[/][[:alnum:]]{8}$'
    chrome_grep = ''
    com = ''.join('find ' + path_to_cache_dir + '| grep ')
    if 'firefox_path' in options:
        com = ''.join(com + firefox_grep)
    elif 'chrome_path' in options:
        com = ''.join(com + chrome_grep)
    else:
        return 'OPTIONS ERROR ON cache_crawler'
    return subprocess.getstatusoutput(com)


# file_inspector(list_of_files, options): recibe una lista de ficheros
# para inspeccionar y una lista de opciones.
# Devuelve una lista de la ruta de cada fichero y su tipo
# Opciones tratadas:
# minsize: (pendiente)
# maxsize: (pendiente)
# type-only: (pendiente)


def file_inspector(list_of_files, options):
    m = magic.Magic()
    Report = [()]
    browser_cache_path = ''
    if 'browser_cache_path' not in options:
        egrep = '[[:alnum:]]{8}.default$'
        com = ''.join('find $HOME | egrep ' + egrep)
        com = subprocess.getstatusoutput(com)
        com = ''.join(com + '/Cache/')
        options[browser_cache_path] = com
    for file in list_of_files:
        filename = ''.join(options[browser_cache_path] + file)
        Report.append(
            [filename, m.from_file(filename + file)])
    return Report