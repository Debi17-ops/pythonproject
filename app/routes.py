# Importing required classes and modules
from flask import Blueprint, request, jsonify
from models import db
from models import Employee
from schema import EmployeeSchema
from marshmallow import ValidationError

# serializing with help of marshmallow
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Main_Blueprint
main = Blueprint('routes',__name__)
@main.route('/')
def home():
    return "Welcome to the Employee Management System"


# Method to Create Employee
@main.route("/employee", methods = ['POST'])
def create_employee():
    if request.content_type != 'application/json':
        return jsonify({'bad-request':'content-type must be "application/json"'})
    
    data = request.get_json()
    new_emp = employee_schema.load(data)
    employee = Employee(name = new_emp['name'],position = new_emp['position'],dept = new_emp['department'])
    db.session.add(employee)
    db.session.commit()
    return employee_schema.dump(employee),201


# Method to get all employees
@main.route("/employee/<int:employee_id>", methods = ['GET'])
def get_employee():
    employees = Employee.query.all()
    return jsonify([{
        'id':employee.id,
        'name':employee.name,
        'positon':employee.position,
        'department':employee.department}for employee in employees])


# Method to update an employee data
@main.route("/employee/<int:employee_id>", methods = ['PUT'])
def update_emp(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message':'employee not found'}),404
    data = request.get_json()
    employee.name = data['name']
    employee.position = data['position']
    employee.department = data['department']
    db.session.commit()
    return jsonify({'message':'employee updated successfully'})


# Method to delete an employee a data
@main.route("/employee/<int:employee_id>", methods = ['DELETE'])
def delete_emp(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message':'employee not found'}),404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message':'employee deleted successfully'})