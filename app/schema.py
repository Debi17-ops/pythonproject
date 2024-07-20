# Importing marshamllow
from marshmallow import Schema, fields, validate

# Instanciating the EmployeeSchema class
class EmployeeSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str(required=True)
    position = fields.Str(required=True)
    department = fields.Str(required=True)