# Importing required classes from modules 
from flask_sqlalchemy import SQLAlchemy

# initializing the SQLAlchemy class
db = SQLAlchemy()


# DEfinining the Employee class
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    position = db.Column(db.String(100), nullable = False)
    department = db.Column(db.String(100), nullable = False)

# init function to initialize the class attributes
    def _init_(self, name, position, department):
        self.name = name
        self.positon = position
        self.department = department


# repr a representory function
    def _repr_(self):
        return f'<Employee{self.name}>'

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'position':self.position,
            'department':self.department
        }