def get_database_url(dbinfo):
    user = dbinfo.get("USER") or "root"
    password =dbinfo.get("PASSWORD") or "911123"
    host = dbinfo.get("HOST") or "127.0.0.1"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or "mysql"
    db = dbinfo.get("DB") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    return "{}+{}://{}:{}@{}:{}/{}".format(db,driver,user,password,host,port,name)

#全局环境配置
class Config(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = "110"
    SESSION_TYPE = "redis"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#开发环境配置
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER" : "root",
        "PASSWORD":"911123",
        "HOST" :"127.0.0.1",
        "PORT" :"3306",
        "NAME" : "test",
        "DB" : "mysql",
        "DRIVER":"pymysql"
    }
    SQLALCHEMY_DATABASE_URI =get_database_url( DATABASE)

#测试环境配置
class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "USER" : "root",
        "PASSWORD":"911123",
        "HOST" :"127.0.0.1",
        "PORT" :"3306",
        "NAME" : "test",
        "DB" : "mysql",
        "DRIVER":"pymysql"
    }
    SQLALCHEMY_DATABASE_URI =get_database_url( DATABASE)


#演示环境配置
class DemoConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER" : "root",
        "PASSWORD":"911123",
        "HOST" :"127.0.0.1",
        "PORT" :"3306",
        "NAME" : "test",
        "DB" : "mysql",
        "DRIVER":"pymysql"
    }
    SQLALCHEMY_DATABASE_URI =get_database_url( DATABASE)


# 线上环境-生产环境配置
class ProductConfig(Config):
    DATABASE = {
        "USER": "root",
        "PASSWORD": "911123",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "test",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)

config = {
    "develop" : DevelopConfig,
    "testing" : TestingConfig,
    "demo"    : DemoConfig,
    "product" : ProductConfig,
    "default" : DevelopConfig
}