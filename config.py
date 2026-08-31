import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'imagesmaaz123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 's96Zi4ukFR/zyJWu4ndY2cFVtDwDZu9uV6lJaD22223E7TKJ2Ao1hCbibRoxLRlMVz8ED1t7j7Dv+AStBARiog=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-maaz.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'admin@123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'Ufm8Q~UcR1Nj1DphCz0JNrK7z4P6G3398TeuKbGI'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"
    CLIENT_ID = os.environ.get('CLIENT_ID') or '8f459c42-7d99-4324-9e7c-d6a6cc377e78'
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app
    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
