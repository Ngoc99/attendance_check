from ../wsgi.app import my_mongo_db as db 

class Staff(db.Document): 
    _id = db.StringField(requried = True)
    sname = db.StringField(required = True)


class Course(db.Document): 
    _id: db.StringField(required = True)
    cname: db.StringField()
    s_id: db.ReferenceField(Staff)

class Department(db.Document): 
    _id: db.StringField(required = True)
    name: db.StringField()
    name_eng: db.StringField()

class Class(db.Document): 
    _id: db.StringField(required = True)
    name: db.StringField(required = True)
    c_id : ReferenceField(Course, required = True)
    d_id: ReferenceField(Department, required= True)
    room: StringField(required = True)
    session_number: IntField()
    start_session: IntField()
    start_time: StringField()
    start_date: DateTimeField()
    end_date: DateTimeField()
    is_scheduled: BooleanField()

    



