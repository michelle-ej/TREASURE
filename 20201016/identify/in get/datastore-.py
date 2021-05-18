import pymysql
import getdata

#資料庫連線
db=pymysql.connect(host="140.131.114.149",user="10656028",passwd="Tpe22553558",db="treasure_team",port=3306,charset='utf8')
cursor=db.cursor()

#辨識結果
result=getdata.result()
#流水號
serial=('SELECT max(Sub_Serial_number) FROM treasure_team.treasure_sub_record')
cursor.execute(serial)
sn=cursor.fetchall()[0][0]+1

#得到點數
getpoint=('SELECT Table_Points FROM treasure_points_table where Table_Type_number="%s"' % result)
cursor.execute(getpoint)
gt=cursor.fetchall()[0][0]


#新增資料
sqlcode=('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points ) ' 
'VALUES (%d,"%s","%s",%.2f)')    

#資料內容
data=(sn,5,result,gt)
cursor.execute(sqlcode % data)

print(data)

#----------------------------------------------------------
db.commit()

db.close()