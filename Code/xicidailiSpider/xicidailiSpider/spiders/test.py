import pymysql



if __name__ == "__main__":
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='19961006', port=3306)
    try:
        cur = db.cursor()
        cur.execute('show databases;')
        data = cur.fetchall()
        # data是元组，试着转换成list，允许修改，这样后面阶段的事情比较容易处理
        listdata = [ name[0] for name in data] # list(data)
        print('show databases执行完毕\n')

        print(listdata)

        result = "mysql" in listdata
        # result = "\'mysql\'\," in data
        print(result)
    except Exception:
        print("连接数据库出错了")
    finally:
        db.close()




