import MySQLdb
import getdata

#資料庫連線
db=MySQLdb.connect(host="140.131.114.149",user="10656028",passwd="Tpe22553558",db="treasure_team",port=3306,charset='utf8')
cursor=db.cursor()

#辨識結果
result=getdata.result()
print(result)

#SQL語法
sqlcode=('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points ) ' 
        'VALUES (%d,"%s","%s",%.2f)')

data=(11,"5",result,0.2)
cursor.execute(sqlcode % data)
#----------------------------------------------------------

db.commit()

db.close()