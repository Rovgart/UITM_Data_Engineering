from basicmmodel import Student, app, db

app.app_context().push()
db.create_all()

stud1=Student("Jacek",6)
stud2=Student("Piotr",7)
stud3=Student("Kamil",7)
print(stud1.id)
print(stud2.id)

db.session.add_all(
    [stud1,stud2,stud3]
)
db.session.commit()

print(stud1.id)
print(stud2.id)

print(stud1)
print(stud2)



