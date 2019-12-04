import pymysql
from scrapy.utils.project import get_project_settings

def create_connection():
    settings = get_project_settings()
    db = pymysql.connect(host=settings['MYSQL_HOST'],
                         user=settings['MYSQL_USER'],
                         passwd=settings['MYSQL_PASS'],
                         port=settings['MYSQL_PORT'],
                         charset=settings['MYSQL_CHARSET'])
    return db

def create_database(settings):
    db = create_connection()
    try:
        cursor = db.cursor()
        cursor.execute("create database " + settings['MYSQL_DB'] + " character set utf8;")
        print("创建"+ settings['MYSQL_DB'] +"库完成")
        return is_exist_database(settings)
    except Exception:
        print("创建数据库出错了")
        return False
    finally:
        db.close()


def is_exist_database(settings):
    print("查看对应数据库是否存在")
    db = create_connection()
    try:
        cursor = db.cursor()
        cursor.execute('show databases;')
        data = cursor.fetchall()
        # data是元组，试着转换成list，允许修改，这样后面阶段的事情比较容易处理
        listdata = [name[0] for name in data]  # list(data)
        # print('show databases执行完毕\n')
        result = settings['MYSQL_DB'] in listdata
        # result = "\'mysql\'\," in data
        return result
    except Exception:
        print("连接数据库出错了")
        return False
    finally:
        db.close()


def is_exist_table(settings):
    db = create_connection()
    try:
        cursor = db.cursor()
        cursor.execute('use '+ settings['MYSQL_DB'] +';')
        print("使用数据库  " + settings['MYSQL_DB'])
        print("show tables")
        cursor.execute("show tables;")
        data = cursor.fetchall()
        listdata = [name[0].upper() for name in data]  # list(data)
        print(listdata)
        # print('show databases执行完毕\n')
        print(settings['MYSQL_TABLE'])
        result = settings['MYSQL_TABLE'] in listdata
        print(result)
        # result = "\'mysql\'\," in data
        return result
    except Exception:
        print("连接数据库出错了")
        return False
    finally:
        db.close()

def create_table(settings):
    print("-------查看表格存在吗---------")
    db = create_connection()

    try:
        cursor = db.cursor()
        cursor.execute('use ' + settings['MYSQL_DB'] + ';')
        print("使用数据库  " + settings['MYSQL_DB'])
        # sqlstatement = "create table " + settings['MYSQL_TABLE'] + " ( " + settings['MYSQL_TABLE_IP'] + " varchar(20),  " + settings['MYSQL_TABLE_PORT'] + " varchar(20) ) character set utf8;"

        sqlstatement = "create table %s ( %s varchar(20),  %s varchar(20) ) character set utf8;" \
                       % (settings['MYSQL_TABLE'], settings['MYSQL_TABLE_IP'], settings['MYSQL_TABLE_PORT'])
        print(sqlstatement)
        cursor.execute(sqlstatement)
        print("创建" + settings['MYSQL_TABLE'] + "表完成")
        return is_exist_table(settings)
    except Exception:
        print("连接数据库出错了")
        return False
    finally:
        db.close()