import MySQLdb as ms
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from sqlalchemy.ext.declarative import declarative_base

eg = create_engine('mysql://asd:1q2w3e4r5t!@localhost/moyu?charset=utf8',convert_unicode=False)
ds = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=eg))

Base = declarative_base()
Base.query = ds.query_property()




ms.connect()