from flask import Flask, request
from flask_restful import Api, Resource
from secure_check import authenticate, identity
from flask_jwt_extended import JWTManager, jwt_required, create_access_token # type: ignore
app=Flask(__name__)
app.config['SECRET_KEY']='mySeCreTKeY'
api=Api(app)

jwt= JWTManager(app)
students=[]

class StudentsName(Resource):
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


class AllStudents(Resource):
    @jwt_required()
    def get(self):
        return {"students":students}

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username, password)

        if not user:
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(identity=str(user.id))
        return {"access_token": access_token}, 200
api.add_resource(StudentsName,'/student/<string:name>')
api.add_resource(AllStudents,'/students')
api.add_resource(Login,'/login')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
