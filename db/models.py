from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,Integer,String,Text,BigInteger,DateTime
from db.db_pool import mysql_engine,metadata

Base = declarative_base()
Session = sessionmaker(bind=mysql_engine)

session = Session()

class Employee_db(Base):
  __tablename__ = 'employee_db'
  employee_id = Column(Integer,primary_key=True)
  employee_name = Column(String(150),nullable=False)
  employee_email = Column(String(150),nullable=False,unique=True)
  employee_phone = Column(BigInteger,nullable=False)
  employee_dob = Column(DateTime)
  employee_gender = Column(String(150),nullable=False)
  employee_address = Column(Text)

Base.metadata.create_all(bind=mysql_engine)