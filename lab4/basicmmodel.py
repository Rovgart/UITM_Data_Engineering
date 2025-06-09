from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

base_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///'+os.path.join(base_dir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    semester=db.Column(db.Integer)
    
    def __init__(self,name,semester):
        self.name=name
        self.semester=semester
        
    def __repr__(self):
        return f"Student {self.name} is studying at {self.semester} semester"