import mysql.connector
import datetime
import requests

# url on which data to be sent
url ="https://sokt.io/zuMeLkivxyDsMyBWJHsW/personal-harish1908"

mydb = mysql.connector.connect(host='localhost',user='root',password='pass@123',database="walkover")
cursor = mydb.cursor()

cursor.execute("SELECT user_userid FROM ms_user WHERE TIMESTAMPDIFF(MINUTE, user_date, now()) BETWEEN 30 AND 60  and user_userid NOT IN ( SELECT userid FROM ms_user_paid_signup)")

#array of unpaid_signup and tim between 30 and 60
userid = cursor.fetchall()

#querry
userdata ="select user_uname,user_email, user_mobno,user_userid from ms_user where user_userid = %s"

for i in range(len(userid)) :
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






             





