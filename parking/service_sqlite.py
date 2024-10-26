import sqlite3
userName="" # 记录用户名
def open():
    try:
        db = sqlite3.connect("./db/car.db")  # 数据库连接
        return db  # 返回连接对象
    except Exception as e:
        print(f"Error opening database connection: {e}")
        return 1  # 如果发生异常，返回1
# 执行数据库的增、删、改操作
def exec(sql, values):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql, values)  # 执行增删改的SQL语句
        db.commit()  # 提交数据
        return 1  # 执行成功
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        print(f"Error executing SQL: {e}")
        return 0  # 执行失败
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭数据库连接

# 带参数的精确查询
def query(sql, *keys):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql, keys)  # 执行查询SQL语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果

# 不带参数的模糊查询
def query2(sql):
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行查询SQL语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果