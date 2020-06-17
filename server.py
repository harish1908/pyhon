import mysql.connector
import datetime
import requests

mydb = mysql.connector.connect(host='localhost',user='root',password='pass@123',database="test")
cursor = mydb.cursor()

cursor.execute("select datetime from employee")

res = cursor.fetchall()
for data in res :
    print(datetime.time())


# data to be sent to an url
data = "hello"

# url on which data to be sent
url ="http://pastebin.com/api/api_post.php"


r=requests.post(url=url, data = data)





