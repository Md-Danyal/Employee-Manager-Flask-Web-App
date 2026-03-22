from flask import Flask,render_template,url_for,redirect,request
from db.repository import EmployeeRepo
# from datetime import datetime

app = Flask(__name__)

emp_obj = EmployeeRepo()

@app.route('/',methods = ["GET","POST"])
def home():
  if request.method == "POST":
    emp_name = request.form.get('employee_name','')
    emp_email = request.form.get('employee_email','')
    emp_phone = request.form.get('employee_phone','')
    emp_dob = request.form.get('employee_dob','')
    emp_gender = request.form.get('employee_gender','')
    emp_address = request.form.get('employee_address','')
    emp_obj.createEmployee(emp_name,emp_email,emp_phone,emp_dob,emp_gender,emp_address)
    return redirect(url_for('home'))

  return render_template('home.html')

@app.route('/views/')
def views_employees():
  employees = emp_obj.getAllEmployee()
  return render_template('views_employees.html',employees=employees)

@app.route('/views/<int:id>',methods=["GET","POST"])
def view_employee(id):
  employee = emp_obj.getOneEmployee(id=id)

  if request.method == "POST":
    emp_id = employee.employee_id
    emp_email = request.form.get('employee_email','')
    emp_phone = request.form.get('employee_phone','')
    emp_address = request.form.get('employee_address','')

    if emp_email != employee.employee_email:
      emp_obj.updateEmail(emp_id,emp_email)

    if emp_phone != employee.employee_phone:
      emp_obj.updatePhone(emp_id,emp_phone)

    if emp_address != employee.employee_address:
      emp_obj.updateAddress(emp_id,emp_address)

    return redirect(url_for('view_employee',id=id))
  return render_template('view_emp.html',employee=employee)

@app.route('/delete/<int:id>')
def delete_employee(id):
  emp_obj.deleteEmployee(id=id)
  return redirect(url_for('views_employees'))

if __name__ == "__main__":
  app.run(debug=True,port=5000)