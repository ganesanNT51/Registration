from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])


class CRUDModel():
	def __init__(self):
		try:
			self.meta = MetaData()
			self.users = Table("users", self.meta, autoload=True, autoload_with=engine)
		except Exception as e:
			print(e)

	def insertData(self,data):
		result = engine.execute(self.users.insert(), data)
		return result