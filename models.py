from peewee import *
from datetime import date

db = SqliteDatabase('classes.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id_user = AutoField()
    name = CharField()
    login = CharField(unique=True)
    password = CharField() 

class Student(BaseModel):
    id_student = AutoField()
    name = CharField()
    email = CharField(unique=True)
    phone = CharField(null=True)
    birthdate = DateField()

class Class(BaseModel):
    id_class = AutoField()
    class_name = CharField()
    id_user = ForeignKeyField(User, backref='classes')
    date = DateField()
    time = TimeField()

class Attendance(BaseModel):
    id = AutoField()
    id_class = ForeignKeyField(Class, backref='attendances')
    id_student = ForeignKeyField(Student, backref='attendances')
    attend = BooleanField()

    class Meta:
        indexes = (
            (('id_class', 'id_student'), True),
        )

def initialize_db():
    with db:
        db.create_tables([User, Student, Class, Attendance])