DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#'django.db.backends.postgresql_psycopg2', #'django.db.backends.sqlite3', # Add , 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ortoloco',#'db.sqlite',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'ortoloco',
        'PASSWORD': 'ortoloco',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}