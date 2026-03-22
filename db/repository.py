from db.models import Employee_db,session

class EmployeeRepo:

  def createEmployee(self,name,email,phone,dob,gender,address):
    employee = Employee_db(employee_name = name,employee_email = email, employee_phone = phone, employee_dob = dob, employee_gender = gender, employee_address = address)
    session.add(employee)
    session.commit()

  def getAllEmployee(self):
    emp = session.query(Employee_db).all()
    return emp
  
  def filterStmt(self,id):
    stmt = session.query(Employee_db).filter_by(employee_id=id).first()
    return stmt

  def getOneEmployee(self,id):
    return self.filterStmt(id)
  
  def updateEmail(self,id,email):
    # emp = session.query(Employee_db).filter_by(employee_id=id).first()
    emp = self.filterStmt(id)
    emp.employee_email = email
    session.commit()

  def updatePhone(self,id,phone):
    self.filterStmt(id).employee_phone = phone
    session.commit()

  def updateAddress(self,id,address):
    self.filterStmt(id).employee_address = address
    session.commit()

  def deleteEmployee(self,id):
    emp = self.filterStmt(id)
    session.delete(emp)
    session.commit()