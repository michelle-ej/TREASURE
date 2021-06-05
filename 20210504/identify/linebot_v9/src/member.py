import db
import app

'''
def create1(line_id,sex):
    db.run(("insert into treasure_member set Member_LINEid=%s, set Member_Gender=%s",line_id,sex),"member_join")
    return db.run(("select * from tablen_name where column_id=%s",line_id),"1")

print('ok2')
'''


def create(line_id,gender,time,phone,address,name):
    db.run("insert into treasure_member (Member_LINEid,Member_Gender,Member_Birthady,Member_Phone,Member_Address,Member_Name) values(\"%s\", \"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %(line_id,gender,time,phone,address,name),"member_join")
    return db.run("select * from treasure_member","2")

'''
def create2(line_id,gender):
    db.run("insert into treasure_member (Member_LINEid,Member_Gender) values(\"line_id\",\"女\")","member_join")
    print("create")
    return db.run("select * from treasure_member","1")
'''


