import pymysql

# host = "localhost"
# user = "root"
# password = ""
# database = "bank"

#增、删、改
def update(sql, param):
    #链接
    con = pymysql.connect(host="localhost", user="root", password="", database="sell")
    cursor = con.cursor()  # 控制台
    cursor.execute(sql, param)

    #数据提交到数据库
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()

def select(sql, param, mode = "all",size=1):
    # 链接
    con = pymysql.connect(host="localhost", user="root", password="", database="sell")
    cursor = con.cursor()  # 控制台
    cursor.execute(sql, param)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany()
    # 数据提交到数据库
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()

def cexcel(sql, param):
    # 链接
    con = pymysql.connect(host="localhost", user="root", password="", database="sell")
    cursor = con.cursor()  # 控制台
    cursor.execute(sql, param)
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()




