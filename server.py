import mysql.connector
import datetime
import requests

# url on which data to be sent
url ="https://sokt.io/TmZf28HY6QaN7FafuPbm/personal-loginflow"

mydb = mysql.connector.connect(host='localhost',user='root',password='pass@123',database="walkover")
cursor = mydb.cursor()

cursor.execute("select userid from ms_user_paid_signup")

#array to store paid userid
paid_id = cursor.fetchall()

cursor.execute("select user_userid from ms_user")

# array of user_userid 
userid = cursor.fetchall()



# list of queries

userdate = "select user_date from ms_user where user_userid = %s "
userdata ="select user_uname,user_email, user_mobno,user_userid from ms_user where user_userid = %s"

for i in range(len(userid)) :
    ser_ele = -1
    for j in range(len(paid_id)) :
        if paid_id[j] == userid[i] :
            ser_ele = j
            break

    if ser_ele < 0 :
        cursor.execute(userdate,userid[i])
        udate = cursor.fetchone()
        diff = (datetime.datetime.now()-udate[0]).total_seconds()
        if diff > 1800 :
            cursor.execute(userdata,userid[i])
            result = cursor.fetchone()
            data = {
                'uname' : result[0],
                'mail' : result[1],
                'mob' : result[2],
                'uid' : result[3]
            }
            r=requests.post(url=url, data = data)
            print(r)

        else :
            print("time less than 30 minutes")

    else :
        print("user has paid signup for uid  %s",userid[i])                





