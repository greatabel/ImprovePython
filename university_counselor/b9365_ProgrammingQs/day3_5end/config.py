class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pwd}@{host}/{database}'.format(
        user=environ.get('DB_USER', 'root'),
        pwd=environ.get('MYSQLCONNSTR_DB_PWD', ''),
        host=environ.get('DB_HOST', 'localhost'),
        database=environ.get('DB_NAME', 'blog_db'),
        charset='utf8mb4',  # The characterset you need
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pwd}@{host}/{database}'.format(
        user=environ.get('DB_USER', 'root'),
        pwd=environ.get('MYSQLCONNSTR_DB_PWD', ''),
        host=environ.get('DB_HOST', 'localhost'),
        database=environ.get('DB_NAME', 'blog_db'),
        charset='utf8mb4',  # The characterset you need
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
