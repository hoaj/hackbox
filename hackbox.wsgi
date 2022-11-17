import sys 
import logging 

logging.basicConfig(level=logging.DEBUG, filename='var/www/html/hackbox/logs/hackbox.log', format='%asctime's %(message)s')
sys.path.insert(0, '/var/www/html/hackbox')
sys.path.insert(0, '/var/www/html/hackbox/hackbox/lib/python3.8/site-package')

from hackbox.hackbox_app import app as application
