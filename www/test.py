import orm
from models import User,Blog,Comment
import asyncio
import mysql.connector

async def test():
	await orm.create_pool(loop=loop,host='127.0.0.1', port=3306, user='www-data',password='www-data',db='awesome')
	u=User(name='Test2',email='test2@example.com',passwd='1234567890',image='about:blank',id='111')
	
	await u.save()
	
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()

coon = mysql.connector.connect(user='www-data', password='www-data', database='awesome')
cursor = coon.cursor()
cursor.execute('select * from users')
print(cursor.fetchall())
