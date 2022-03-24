from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])


class UserModel():
	def __init__(self):
		try:
			self.meta = MetaData()
			self.users = Table("users", self.meta, autoload=True, autoload_with=engine)
			self.states = Table("states", self.meta, autoload=True, autoload_with=engine)            
		except Exception as e:
			print(e)

	def insert_users(self,data):
		result = engine.execute(self.users.insert(), data)
		return result

	def get_states(self):
		print('in Get Function')
		stmt = select([self.states])
		result = engine.execute(stmt)
		return result

	def get_users(self):
		print('in Get Function')
		stmt = select([self.users])
		result = engine.execute(stmt)
		return result	

	def get_users_email(self,email):
		stmt = self.users.select().where(self.users.c.email.in_([email]))
		result = engine.execute(stmt)
		result = result.fetchone()
		if result :
			return "success"
		else:
			return "fail"   


			

	def get_users_mobile(self,mobile):
		stmt = self.users.select().where(self.users.c.mobile.in_([mobile]))
		result = engine.execute(stmt)
		result = result.fetchone()
		if result :
			return "success"
		else:
			return "fail" 


	# get_users_email_data 
	def get_users_email_data(self,email):
		stmt = self.users.select().where(self.users.c.email.in_([email]))
		results = engine.execute(stmt)
		results = [dict(r) for r in results] if results else None
		if results : 
			return results[0]
		else:
			return None

	def update_last_login(self,user_id,last_login):
		stmt = self.users.update().values({"last_login":last_login}).where(self.users.c.user_id.in_([user_id]))
		result = engine.execute(stmt)
		return result

	def delete_user(self,id):
		print('in Delete Function')
		print(id)
		stmt = self.users.delete().where(self.users.c.user_id.in_([id]))
		result = engine.execute(stmt)
		return result		

	def edit_user(self,id):
		print('in Edit Function')
		print(id)
		stmt = select([self.users]).where(self.users.c.user_id.in_([id]))
		result = engine.execute(stmt)
		output = result.fetchone()
		return output  

	def update_user(self,id,data):
		stmt = self.users.update().where(self.users.c.user_id.in_([id])).values(data)
		result = engine.execute(stmt)
		if result:
			return 'success'
		else :
		   return 'fail'


	def check_users_email_for_update(self,email,user_id):
		stmt = text("select count(*) as email_count from users where email = "+"'"+email+"' "+"and user_id != "+str(user_id)  +";")
		result = engine.execute(stmt)
		results = [dict(r) for r in result] if result else None
		print(results[0])
		if results :
			return results[0]
		else:
			return None 	  


			

	def check_users_mobile_for_update(self,mobile,user_id):
		stmt = text("select count(*) as mobile_count from users where mobile = "+"'"+mobile+"' "+"and user_id != "+ str(user_id)  +";")
		result = engine.execute(stmt)
		results = [dict(r) for r in result] if result else None
		print(results)
		if results :
			return results[0]
		else:
			return None		


	def get_username(self,user_id):
		stmt = text("select name  from users where user_id = "+str(user_id)+";")
		result = engine.execute(stmt)
		results = [dict(r) for r in result] if result else None
		print(results)
		if results :
			return results[0]
		else:
			return None		   	  		              