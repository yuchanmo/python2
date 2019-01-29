from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Student(Base):
  _tablename_ = 'tbTable'
  id = Column(String(5), primary_key=True)
  name = Column(String(20))
  name = Column(String(20))
  string = Column(String(250))
  
  def __init__(self, datetime, string):
    self.datetime = datetime
    self.string = string
    
  def __repr__(self):
    return "<TbTest('%d', '%s', '%s'>" %(self.id, str(self.datetime), self.string)

