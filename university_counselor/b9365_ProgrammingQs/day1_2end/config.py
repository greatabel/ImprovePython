from os import environ


class Config(object):
    pass


class ProdConfig(Config):
    pass


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


