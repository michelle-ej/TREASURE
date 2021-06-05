import db
print('no1')
# 執行 MySQL 查詢指令

def searchMemberById(line_id):
    print('12434343434')
    return db.run(("SELECT Record_Recycling_number FROM treasure_recycling_record where Record_LINEid = '%s'" %(line_id)),"1")
    
# 輸出結果