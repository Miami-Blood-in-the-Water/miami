r"""
Evennia settings file.

The available options are found in the default settings file found
here:

c:\users\joe\src\evennia\evennia\settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
import json

import boto3
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

INSTALLED_APPS = INSTALLED_APPS + [
    "character"
]

# This is the name of your game. Make it catchy!
SERVERNAME = "miami"

"""
try:
    client = boto3.client('secretsmanager')
    secret = client.get_secret_value(SecretId='prod/postgres/miami')
    database = json.loads(secret['SecretString'])
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': database['dbname'],
            'USER': database['username'],
            'PASSWORD': database['password'],
            'HOST': database['host'],
            'PORT': database['port']
        }}
except Exception:
    pass
"""

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
