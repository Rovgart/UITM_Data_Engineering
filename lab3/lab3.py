from flask import Flask
from flask_restful import Api, Resource

app= Flask(__name__)
api=Api(app)
students=[]
class AllStudents(Resource):
     def get(self):
        return {"students":students}

class StudentIndividual(Resource):
    def get(self,name):
          for stud in students:
            if students["name"]==name:
                return stud
            return {'name':None}, 404
    
    def post(self,name):
        stud={
            "name":name
        }
        students.append(stud)
        return stud
    def delete(self, name):
        for i, stud in enumerate(students):
            if stud["name"]==name:
                deleted_stud=students.pop(i)
                return {
                    "info":"Successfully deleted"
                }


api.add_resource(AllStudents,'/students')
api.add_resource(StudentIndividual,'/student/<string:name>')

if __name__ == '__main__':
    app.run(debug=True, port=3000)

