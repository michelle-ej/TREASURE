import pymysql
import app
# 連接 MySQL 資料庫
print('ok')


def run(sql,type):
    db = pymysql.connect(host="127.0.0.1",user="root", passwd="NTUB10656051", db="treasure_team",port=3306,charset='utf8mb4')
    cursor = db.cursor()
    print("db\t %s" %(sql))
    cursor.execute(sql)
    if(type=="1"):
        return cursor.fetchall()
    db.commit()
    db.close()
    






print('ok1')


# 關閉連線
