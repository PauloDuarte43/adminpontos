import os
import sys
import site

python_home = '/usr/local/venvs/adminpontos'

site.addsitedir(python_home + '/lib/python2.7/site-packages')

sys.path.append('/var/www/adminpontos')
sys.path.append('/var/www/adminpontos/admin')

os.environ['TZ'] = 'America/Sao_Paulo'

activate_env=os.path.expanduser(python_home + '/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from admin import app as application
