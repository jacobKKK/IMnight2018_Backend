#import all default settings.
from .settings import *

STATIC_URL = '/static/IMnight/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Allow all host headers.
ALLOWED_HOSTS = ['140.112.106.45','ntu.im']

# Turn off DEBUG mode.
#DEBUG = False
