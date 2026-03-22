from sqlalchemy import create_engine,MetaData

URL = 'mysql+mysqlconnector://root:root@localhost:3306/employee_db'
mysql_engine = create_engine(url=URL,echo=True)

metadata = MetaData()